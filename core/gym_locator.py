"""Core Gym & Fitness Center Locator Service for TRUFORM AI.

Provides device geolocation resolution, nearby gym discovery via OpenStreetMap Overpass API,
Haversine distance calculation, geocoding for custom city searches, and 1-click Google Maps integration.
"""

import json
import math
import os
import urllib.parse
import urllib.request
from typing import Dict, Any, List, Optional, Tuple
import webbrowser

# Cache file path for persisting last known device location
_CACHE_PATH = os.path.join(os.path.dirname(__file__), "..", ".user_location.json")

# Default fallback location: Noida, Uttar Pradesh (default project context)
DEFAULT_LOCATION = {
    "lat": 28.4744,
    "lon": 77.5040,
    "city": "Greater Noida",
    "region": "Uttar Pradesh",
    "country": "India",
    "ip": "Local Device",
    "is_fallback": True
}


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculates great-circle distance (in kilometers) between two coordinates
    using the Haversine formula.
    """
    r = 6371.0  # Earth radius in kilometers

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2.0) ** 2 +
         math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2.0) ** 2))
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    return round(r * c, 2)


def get_cached_location() -> Optional[Dict[str, Any]]:
    """Retrieves cached device location if available."""
    try:
        if os.path.exists(_CACHE_PATH):
            with open(_CACHE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "lat" in data and "lon" in data:
                    return data
    except Exception:
        pass
    return None


def save_cached_location(location: Dict[str, Any]):
    """Caches device location to local disk for fast subsequent loads."""
    try:
        with open(_CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(location, f, indent=2)
    except Exception:
        pass


def get_device_location() -> Dict[str, Any]:
    """
    Resolves the current device geographical coordinates and location details.
    Tries multiple IP geolocation providers with timeout and cached fallback.
    """
    headers = {"User-Agent": "TruFormAI/1.0 (Athletic Motion Intelligence)"}

    # Provider 1: ip-api.com (HTTP, fast, returns structured lat/lon)
    try:
        req = urllib.request.Request("http://ip-api.com/json/?fields=status,message,country,regionName,city,lat,lon,query", headers=headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            payload = json.loads(response.read().decode("utf-8"))
            if payload.get("status") == "success":
                loc = {
                    "lat": float(payload["lat"]),
                    "lon": float(payload["lon"]),
                    "city": payload.get("city", "Unknown City"),
                    "region": payload.get("regionName", ""),
                    "country": payload.get("country", ""),
                    "ip": payload.get("query", ""),
                    "is_fallback": False
                }
                save_cached_location(loc)
                return loc
    except Exception:
        pass

    # Provider 2: freeipapi.com (HTTPS, free, generous limit)
    try:
        req = urllib.request.Request("https://freeipapi.com/api/json", headers=headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            payload = json.loads(response.read().decode("utf-8"))
            if "latitude" in payload and "longitude" in payload:
                loc = {
                    "lat": float(payload["latitude"]),
                    "lon": float(payload["longitude"]),
                    "city": payload.get("cityName", "Unknown City"),
                    "region": payload.get("regionName", ""),
                    "country": payload.get("countryName", ""),
                    "ip": payload.get("ipAddress", ""),
                    "is_fallback": False
                }
                save_cached_location(loc)
                return loc
    except Exception:
        pass

    # Provider 3: ipapi.co (HTTPS fallback)
    try:
        req = urllib.request.Request("https://ipapi.co/json/", headers=headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            payload = json.loads(response.read().decode("utf-8"))
            if "latitude" in payload and "longitude" in payload:
                loc = {
                    "lat": float(payload["latitude"]),
                    "lon": float(payload["longitude"]),
                    "city": payload.get("city", "Unknown City"),
                    "region": payload.get("region", ""),
                    "country": payload.get("country_name", ""),
                    "ip": payload.get("ip", ""),
                    "is_fallback": False
                }
                save_cached_location(loc)
                return loc
    except Exception:
        pass

    # Cached Location fallback
    cached = get_cached_location()
    if cached:
        cached["is_fallback"] = True
        return cached

    # Static default fallback
    return dict(DEFAULT_LOCATION)


def geocode_location(query: str) -> Optional[Dict[str, Any]]:
    """
    Resolves custom city, district, or address query into (lat, lon) coordinates
    using OpenStreetMap Nominatim.
    """
    if not query or not query.strip():
        return None

    clean_query = query.strip()
    encoded = urllib.parse.quote(clean_query)
    url = f"https://nominatim.openstreetmap.org/search?q={encoded}&format=json&limit=1&addressdetails=1"
    headers = {"User-Agent": "TruFormAI/1.0 (Athletic Motion Intelligence)"}

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data and len(data) > 0:
                first = data[0]
                addr = first.get("address", {})
                city = (addr.get("city") or addr.get("town") or addr.get("suburb") or
                        addr.get("state_district") or clean_query)
                region = addr.get("state", "")
                country = addr.get("country", "")
                return {
                    "lat": float(first["lat"]),
                    "lon": float(first["lon"]),
                    "display_name": first.get("display_name", clean_query),
                    "city": city,
                    "region": region,
                    "country": country,
                    "is_fallback": False
                }
    except Exception:
        pass

    return None


def fetch_nearby_gyms(
    lat: float,
    lon: float,
    radius_km: float = 5.0,
    limit: int = 25
) -> List[Dict[str, Any]]:
    """
    Queries OpenStreetMap Overpass API for gyms, fitness centers, and health clubs
    within the specified radius around (lat, lon).
    Returns list of gyms sorted by distance ascending.
    """
    radius_meters = int(radius_km * 1000)

    # Overpass QL query targeting fitness centres, gyms, and sports health centres
    query = f"""
    [out:json][timeout:15];
    (
      node["leisure"="fitness_centre"](around:{radius_meters},{lat},{lon});
      node["amenity"="gym"](around:{radius_meters},{lat},{lon});
      node["leisure"="sports_centre"](around:{radius_meters},{lat},{lon});
      way["leisure"="fitness_centre"](around:{radius_meters},{lat},{lon});
      way["amenity"="gym"](around:{radius_meters},{lat},{lon});
    );
    out center {limit};
    """

    url = "https://overpass-api.de/api/interpreter"
    data_encoded = urllib.parse.urlencode({"data": query}).encode("utf-8")
    headers = {
        "User-Agent": "TruFormAI/1.0 (Athletic Motion Intelligence)",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    results: List[Dict[str, Any]] = []

    try:
        req = urllib.request.Request(url, data=data_encoded, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
            elements = payload.get("elements", [])

            for el in elements:
                tags = el.get("tags", {})
                name = tags.get("name") or tags.get("brand")

                # Extract coordinates (nodes have lat/lon directly; ways have center)
                g_lat = el.get("lat") or el.get("center", {}).get("lat")
                g_lon = el.get("lon") or el.get("center", {}).get("lon")

                if g_lat is None or g_lon is None:
                    continue

                g_lat = float(g_lat)
                g_lon = float(g_lon)
                dist = calculate_distance(lat, lon, g_lat, g_lon)

                # Skip if beyond radius
                if dist > radius_km:
                    continue

                if not name:
                    # Provide intuitive name from tags
                    leisure_type = tags.get("leisure", "").replace("_", " ").title()
                    name = f"Fitness Center ({leisure_type})" if leisure_type else "Community Gym / Fitness Center"

                street = tags.get("addr:street", "")
                housenumber = tags.get("addr:housenumber", "")
                city_addr = tags.get("addr:city", "")
                postcode = tags.get("addr:postcode", "")

                address_parts = [p for p in [housenumber, street, city_addr, postcode] if p]
                address = ", ".join(address_parts) if address_parts else tags.get("address", "")

                results.append({
                    "id": el.get("id"),
                    "name": name,
                    "lat": g_lat,
                    "lon": g_lon,
                    "distance_km": dist,
                    "address": address or "Address available on map",
                    "opening_hours": tags.get("opening_hours", ""),
                    "phone": tags.get("phone") or tags.get("contact:phone", ""),
                    "website": tags.get("website") or tags.get("contact:website", ""),
                    "brand": tags.get("brand", "")
                })

    except Exception:
        pass

    # Sort results by distance (closest first)
    results.sort(key=lambda x: x["distance_km"])
    return results[:limit]


def get_google_maps_search_url(lat: Optional[float] = None, lon: Optional[float] = None, query: str = "gyms near me") -> str:
    """Generates a Google Maps search URL centered on coordinates."""
    if lat is not None and lon is not None:
        return f"https://www.google.com/maps/search/gyms/@{lat:.6f},{lon:.6f},14z"
    q_enc = urllib.parse.quote(query)
    return f"https://www.google.com/maps/search/?api=1&query={q_enc}"


def get_google_maps_directions_url(gym_name: str, gym_lat: float, gym_lon: float) -> str:
    """Generates a Google Maps directions URL to a specific gym."""
    dest_name = urllib.parse.quote(gym_name)
    return f"https://www.google.com/maps/dir/?api=1&destination={gym_lat:.6f},{gym_lon:.6f}&destination_place_id={dest_name}"


def open_url_in_browser(url: str) -> bool:
    """Opens a URL in the user's default web browser safely."""
    try:
        webbrowser.open(url, new=2)
        return True
    except Exception:
        return False

