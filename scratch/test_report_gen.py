import os
import sys
from pathlib import Path

# Add root directory to sys.path
root_dir = str(Path(__file__).resolve().parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import time
from backend.reporter import generate_report_image

test_stats_squat = {
    "clean_reps": 12,
    "failed_depth": 1,
    "failed_sitting": 0,
    "posture_warnings": 1,
    "total_attempts": 13,
    "accuracy": 92,
    "start_time": time.time() - 145,
    "left_arm_reps": 0,
    "right_arm_reps": 0
}

test_stats_deadlift = {
    "clean_reps": 6,
    "failed_depth": 2,
    "failed_sitting": 1,
    "posture_warnings": 2,
    "total_attempts": 9,
    "accuracy": 66,
    "start_time": time.time() - 88,
    "left_arm_reps": 0,
    "right_arm_reps": 0
}

test_stats_curl = {
    "clean_reps": 4,
    "failed_depth": 5,
    "failed_sitting": 0,
    "posture_warnings": 1,
    "total_attempts": 9,
    "accuracy": 44,
    "start_time": time.time() - 65,
    "left_arm_reps": 4,
    "right_arm_reps": 4
}

out1 = generate_report_image("SQUAT", test_stats_squat, "scratch/test_squat_report.png")
out2 = generate_report_image("DEADLIFT", test_stats_deadlift, "scratch/test_deadlift_report.png")
out3 = generate_report_image("BICEP_CURL", test_stats_curl, "scratch/test_bicep_report.png")

print(f"Generated: {out1}, {out2}, {out3}")
