"""Biomechanical posture classification and gesture recognition."""

import numpy as np
from typing import Tuple, Optional


def classify_sitting(
    hip: np.ndarray,
    knee: np.ndarray,
    ankle: np.ndarray
) -> Tuple[bool, float, float]:
    """
    Differentiates passive chair sitting vs. active squat mechanics.
    Criteria: Vertical tibia (<12 deg), horizontal femur (>72 deg), hip above knee crease (< -15px).
    """
    femur_vec = knee - hip
    tibia_vec = ankle - knee

    thigh_angle = float(np.abs(np.degrees(np.arctan2(femur_vec[0], femur_vec[1]))))
    shin_angle = float(np.abs(np.degrees(np.arctan2(tibia_vec[0], tibia_vec[1]))))
    hip_knee_y_diff = float(hip[1] - knee[1])

    # Chair sitting criteria
    is_sitting = (shin_angle < 12.0) and (thigh_angle > 72.0) and (hip_knee_y_diff < -15)
    return bool(is_sitting), thigh_angle, shin_angle


def check_hands_up_gesture(
    kpts: np.ndarray,
    confs: np.ndarray,
    gesture_start_time: Optional[float],
    current_time: float,
    hold_threshold: float = 1.5
) -> Tuple[bool, float, Optional[float]]:
    """
    Detects hands-up reset gesture: both wrists above nose held for hold_threshold seconds.
    Returns: (is_triggered, progress_fraction [0.0 - 1.0], updated_gesture_start_time)
    """
    nose, lwrist, rwrist = kpts[0], kpts[9], kpts[10]
    hands_up = False

    if min(confs[0], confs[9], confs[10]) > 0.4:
        if lwrist[1] < nose[1] and rwrist[1] < nose[1]:
            hands_up = True

    if hands_up:
        if gesture_start_time is None:
            gesture_start_time = current_time
        hold_duration = current_time - gesture_start_time
        progress = min(hold_duration / hold_threshold, 1.0)
        return hold_duration >= hold_threshold, progress, gesture_start_time

    return False, 0.0, None
