"""Presentation layer package containing themes, components, and the main window."""

from .theme import setup_theme
from .app import AIWorkoutUI, run_app

__all__ = ["setup_theme", "AIWorkoutUI", "run_app"]
