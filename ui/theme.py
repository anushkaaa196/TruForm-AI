"""UI theme, color palettes, and typography configurations.

Designed for professional sports science, athletic performance labs,
and clinical biomechanics research.
Warm Charcoal + Deep Navy + Muted Steel Blue Design System.
"""

import customtkinter as ctk

# ==============================================================================
# BASE SURFACES (70% Sophisticated Dark Neutrals)
# ==============================================================================
COLOR_BG_DARK = "#0B1220"          # Main Application Background (Midnight Navy)
COLOR_BG = COLOR_BG_DARK           # Application Background alias
COLOR_WORKSPACE = "#0E1726"        # Main Workspace / Viewport Backing
COLOR_PANEL_BG = "#111C2E"         # Primary Panel, Sidebar, and Header Bar Surface
COLOR_CARD_BG = "#162338"          # Secondary Card Background
COLOR_CARD_ELEVATED = "#1B2A42"    # Elevated Card Background & Interactive Panels
COLOR_CARD_HOVER = "#1B2A42"       # Standard Card Hover
COLOR_CARD_INNER = "#111C2E"       # Video Viewport Inset & Inset Containers
COLOR_CARD_ALT = "#111C2E"         # Dark Inset Panel / Recessed Track
COLOR_PROGRESS_BG = "#0B1220"      # Background Track for Progress Bars
COLOR_STATUS_BG = "#111C2E"        # Live Coach Console Surface

# ==============================================================================
# BORDERS & DIVIDERS
# ==============================================================================
COLOR_BORDER = "#263852"           # Subtle Border
COLOR_BORDER_LIGHT = "#35506F"     # Hover Border / Interactive Outline
COLOR_BORDER_ACTIVE = "#3B82F6"    # Strong Active Border
COLOR_BORDER_ACCENT = "#14B8A6"    # Teal Accent Border Focus
COLOR_DIVIDER = "#1E2C42"          # Separator Lines & Horizontal Rules

# ==============================================================================
# PURPOSEFUL ACCENTS (20% Teal & Blue)
# ==============================================================================
# Primary Brand Accent — Deep Teal
COLOR_TEAL = "#14B8A6"             # Deep Teal
COLOR_TEAL_HOVER = "#0D9488"       # Teal Hover
COLOR_TEAL_MUTED = "#0F3838"       # Teal Pill Background Inset
COLOR_ACCENT = COLOR_TEAL          # Primary Interface Accent
COLOR_ACCENT_HOVER = COLOR_TEAL_HOVER
COLOR_ACCENT_SOFT = "#2DD4BF"      # Soft Bright Teal
COLOR_ACCENT_MUTED = COLOR_TEAL_MUTED

# Primary Action — Professional Blue
COLOR_BLUE = "#3B82F6"             # Professional Blue
COLOR_BLUE_HOVER = "#2563EB"       # Blue Hover
COLOR_BLUE_MUTED = "#1E293B"       # Blue Pill Background Inset
COLOR_PRIMARY = COLOR_BLUE         # Primary Action Blue
COLOR_PRIMARY_HOVER = COLOR_BLUE_HOVER

# ==============================================================================
# SEMANTIC STATUS & PERFORMANCE (10% Semantic Pop Colors)
# ==============================================================================
# Success — Emerald: Clean reps, 90%+ score, optimal alignment
COLOR_SUCCESS = "#22C55E"          # Vibrant Emerald
COLOR_SUCCESS_HIGHLIGHT = "#4ADE80"# Emerald Highlight
COLOR_SUCCESS_HOVER = "#16A34A"    # Darker Emerald
COLOR_SUCCESS_MUTED = "#0D3322"    # Emerald Pill Inset Background

# Attention / Coaching — Amber: Form adjustment cues, moderate risk, warnings
COLOR_WARN = "#F59E0B"             # Warm Amber
COLOR_WARN_HOVER = "#D97706"       # Deep Amber Hover
COLOR_WARN_MUTED = "#3D2808"       # Amber Pill Inset Background

# Critical — Refined Red: Severe misalignment, stop workout, safety alerts
COLOR_ALERT = "#EF4444"            # Refined Red
COLOR_ALERT_HOVER = "#DC2626"      # Deep Crimson Hover
COLOR_ALERT_MUTED = "#3D1418"      # Alert Pill Inset Background

# ==============================================================================
# WORKOUT CONTROLS & ACTION BUTTONS
# ==============================================================================
COLOR_BTN_START = "#16A34A"        # Start Workout Background (Energetic Emerald)
COLOR_BTN_START_HOVER = "#22C55E"  # Start Workout Hover
COLOR_BTN_STOP = "#B91C1C"         # Stop Workout Background (Restrained Red)
COLOR_BTN_STOP_HOVER = "#DC2626"   # Stop Workout Hover
COLOR_BTN_EXPORT = "#2563EB"       # Export Report Background (Professional Blue)
COLOR_BTN_EXPORT_HOVER = "#3B82F6" # Export Report Hover

COLOR_BUTTON_PRIMARY = COLOR_BLUE
COLOR_BUTTON_PRIMARY_HOVER = COLOR_BLUE_HOVER
COLOR_DANGER = COLOR_BTN_STOP
COLOR_DANGER_HOVER = COLOR_BTN_STOP_HOVER
COLOR_INFO = COLOR_BTN_EXPORT
COLOR_INFO_HOVER = COLOR_BTN_EXPORT_HOVER
COLOR_SECONDARY_BTN = "#162338"    # Reset Metrics & Inactive Control
COLOR_SECONDARY_BTN_HOVER = "#1B2A42"
COLOR_BUTTON_SECONDARY = COLOR_SECONDARY_BTN
COLOR_BUTTON_SECONDARY_HOVER = COLOR_SECONDARY_BTN_HOVER

# ==============================================================================
# TYPOGRAPHY SPECIFICATIONS
# ==============================================================================
COLOR_TEXT_PRIMARY = "#F8FAFC"     # Primary Text (Clean Crisp White)
COLOR_TEXT_SECONDARY = "#94A3B8"   # Secondary Text (Cool Slate Gray)
COLOR_TEXT_MUTED = "#64748B"       # Muted Text (Neutral Mid Gray)
COLOR_WHITE = "#FFFFFF"            # White
COLOR_MUTED = "#94A3B8"            # Cool Slate Alias

FONT_FAMILY = "Segoe UI"

FONT_HERO = (FONT_FAMILY, 30, "bold")
FONT_TITLE = (FONT_FAMILY, 15, "bold")
FONT_BRAND = (FONT_FAMILY, 18, "bold")
FONT_BRAND_BADGE = (FONT_FAMILY, 8, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 11)
FONT_BODY = (FONT_FAMILY, 11)
FONT_BODY_BOLD = (FONT_FAMILY, 11, "bold")
FONT_SECTION_HEADER = (FONT_FAMILY, 10, "bold")
FONT_OPTION_MENU = (FONT_FAMILY, 11, "bold")
FONT_STAT_TITLE = (FONT_FAMILY, 9, "bold")
FONT_STAT_LARGE = (FONT_FAMILY, 30, "bold")
FONT_STAT_MEDIUM = (FONT_FAMILY, 20, "bold")
FONT_STAT_SUB = (FONT_FAMILY, 10)
FONT_BUTTON = (FONT_FAMILY, 11, "bold")
FONT_BUTTON_LARGE = (FONT_FAMILY, 12, "bold")
FONT_BUTTON_MEDIUM = (FONT_FAMILY, 11, "bold")
FONT_COACH_TAG = (FONT_FAMILY, 10, "bold")
FONT_COACH_MESSAGE = (FONT_FAMILY, 12, "bold")
FONT_VIEWPORT_TITLE = (FONT_FAMILY, 12, "bold")
FONT_BADGE = (FONT_FAMILY, 9, "bold")
FONT_FEEDBACK = (FONT_FAMILY, 11, "bold")
FONT_TITLE_BAR = (FONT_FAMILY, 13, "bold")
FONT_FOOTER = (FONT_FAMILY, 9)



def setup_theme():
    """Initializes CustomTkinter appearance mode and base theme."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
