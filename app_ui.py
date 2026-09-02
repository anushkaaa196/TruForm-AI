#!/usr/bin/env python3
"""
AI Biomechanics & Posture Analyzer
Backward-compatible entry point that delegates to the modular architecture.
"""

from config import EXERCISE_CONFIGS
from core import (
    LowPassFilter,
    calculate_angle,
    extract_valid_profile,
    classify_sitting,
    check_hands_up_gesture
)
from backend import CameraManager, WorkoutEngine, generate_report_image
from ui import AIWorkoutUI, run_app

__all__ = [
    "AIWorkoutUI",
    "run_app",
    "EXERCISE_CONFIGS",
    "LowPassFilter",
    "calculate_angle",
    "extract_valid_profile",
    "classify_sitting",
    "check_hands_up_gesture",
    "CameraManager",
    "WorkoutEngine",
    "generate_report_image"
]

if __name__ == "__main__":
    run_app()