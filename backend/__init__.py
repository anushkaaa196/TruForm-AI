"""Backend package containing camera capture, pose tracking engine, and reporting."""

from .camera import CameraManager
from .reporter import generate_report_image
from .engine import WorkoutEngine

__all__ = [
    "CameraManager",
    "generate_report_image",
    "WorkoutEngine"
]
