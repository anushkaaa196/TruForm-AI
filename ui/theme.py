"""UI theme, color palettes, and typography configurations."""

import customtkinter as ctk

# Color Palette
COLOR_PRIMARY = "#00C853"        # Green (Start workout)
COLOR_PRIMARY_HOVER = "#009624"
COLOR_DANGER = "#D50000"         # Red (Stop / Reset)
COLOR_DANGER_HOVER = "#9B0000"
COLOR_INFO = "#304FFE"           # Blue (Export report)
COLOR_INFO_HOVER = "#1A237E"

COLOR_ACCENT = "#00FFC8"         # Bright Teal
COLOR_WARN = "#FF9100"           # Amber / Warning
COLOR_ALERT = "#FF1744"          # Deep Red / Disqualification
COLOR_SUCCESS = "#00E676"        # Bright Green / Clean Rep

COLOR_CARD_BG = "#1E1E24"        # Dark charcoal card background
COLOR_STATUS_BG = "#23232A"      # Bottom status bar background
COLOR_MUTED = "#A0A0A0"          # Subtitle / muted text
COLOR_WHITE = "#FFFFFF"

# Fonts
FONT_BRAND = ("Helvetica", 22, "bold")
FONT_SUBTITLE = ("Helvetica", 12)
FONT_SECTION_HEADER = ("Helvetica", 12, "bold")
FONT_OPTION_MENU = ("Helvetica", 13, "bold")
FONT_STAT_TITLE = ("Helvetica", 11)
FONT_STAT_LARGE = ("Helvetica", 36, "bold")
FONT_STAT_MEDIUM = ("Helvetica", 20, "bold")
FONT_BUTTON_LARGE = ("Helvetica", 14, "bold")
FONT_BUTTON_MEDIUM = ("Helvetica", 12)
FONT_COACH_TAG = ("Helvetica", 12, "bold")
FONT_COACH_MESSAGE = ("Helvetica", 14, "bold")


def setup_theme():
    """Initializes CustomTkinter appearance mode and color theme."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
