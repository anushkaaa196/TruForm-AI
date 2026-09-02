"""Diagnostics report card generator."""

import time
import cv2
import numpy as np
from typing import Dict, Any


def generate_report_image(
    exercise_name: str,
    stats: Dict[str, Any],
    output_path: str = None
) -> str:
    """
    Generates and exports an off-screen session diagnostics report image.
    Returns the saved image file path.
    """
    clean_reps = stats.get("clean_reps", 0)
    failed_depth = stats.get("failed_depth", 0)
    failed_sitting = stats.get("failed_sitting", 0)
    posture_warnings = stats.get("posture_warnings", 0)
    start_time = stats.get("start_time")

    total = clean_reps + failed_depth + failed_sitting
    acc = int((clean_reps / max(total, 1)) * 100) if total > 0 else 0

    duration = time.time() - (start_time if start_time else time.time())
    duration_str = f"{int(duration // 60):02d}:{int(duration % 60):02d}"

    card = np.zeros((450, 600, 3), dtype=np.uint8)
    card[:] = (30, 30, 36)
    cv2.rectangle(card, (5, 5), (595, 445), (65, 65, 80), 2)

    cv2.putText(card, f"EXERCISE SUMMARY: {exercise_name}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 200), 2)
    cv2.putText(card, f"Active Time: {duration_str}", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (160, 160, 160), 1)

    # Reps Card
    cv2.rectangle(card, (30, 105), (180, 185), (42, 42, 50), -1)
    cv2.putText(card, "CLEAN REPS", (45, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)
    cv2.putText(card, str(clean_reps), (45, 170), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 2)

    # Attempts Card
    cv2.rectangle(card, (210, 105), (360, 185), (42, 42, 50), -1)
    cv2.putText(card, "ATTEMPTS", (225, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)
    cv2.putText(card, str(total), (225, 170), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 255), 2)

    # Accuracy Card
    cv2.rectangle(card, (390, 105), (540, 185), (42, 42, 50), -1)
    cv2.putText(card, "ACCURACY", (405, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)
    cv2.putText(card, f"{acc}%", (405, 170), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 200), 2)

    # Breakdown Diagnostics
    cv2.putText(card, "Diagnostic Breakdown:", (30, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 220, 220), 1)
    cv2.putText(card, f"- Incomplete Range of Motion: {failed_depth}", (40, 265), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 180, 255), 1)
    cv2.putText(card, f"- Passive Sitting / Chair Disqualifications: {failed_sitting}", (40, 295), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 255), 1)
    cv2.putText(card, f"- Posture / Back Lean Warnings: {posture_warnings}", (40, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 255), 1)

    if output_path is None:
        output_path = f"report_{exercise_name}_{int(time.time())}.png"

    cv2.imwrite(output_path, card)
    return output_path
