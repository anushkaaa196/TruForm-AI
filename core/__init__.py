"""Core biomechanics, math, and filtering package."""

from .filters import LowPassFilter
from .geometry import calculate_angle, extract_valid_profile, extract_exercise_data
from .biomechanics import classify_sitting, check_hands_up_gesture

__all__ = [
    "LowPassFilter",
    "calculate_angle",
    "extract_valid_profile",
    "extract_exercise_data",
    "classify_sitting",
    "check_hands_up_gesture"
]
