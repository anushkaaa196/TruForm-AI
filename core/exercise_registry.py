"""Centralized Exercise Registry & Scalable Capability Architecture.

Provides structured metadata, category classifications, muscle mappings, and capability states
for both Live AI Analyzed exercises and Guided Training Mode exercises.
"""

from typing import Dict, Any, List, Optional
import os


EXERCISE_REGISTRY: Dict[str, Dict[str, Any]] = {
    # ==========================================================================
    # 🟢 ACTIVE AI ANALYSIS EXERCISES (Full YOLO Rep & Angle Tracking)
    # ==========================================================================
    "SQUAT": {
        "id": "SQUAT",
        "name": "Squat",
        "display_name": "Bodyweight / Barbell Squat",
        "category": "Lower Body",
        "difficulty": "Beginner",
        "primary_muscles": ["Quadriceps", "Gluteus Maximus"],
        "secondary_muscles": ["Hamstrings", "Core Stabilizers", "Calves"],
        "analysis_status": "ACTIVE",
        "status_label": "🟢 LIVE AI ANALYSIS AVAILABLE",
        "status_badge": "ACTIVE AI",
        "status_description": "Full real-time YOLOv8 pose tracking, parallel depth validation, and rep counting.",
        "description": "Fundamental lower-body compound movement developing leg strength, hip mobility, and spinal stability.",
        "form_reference": os.path.join("assets", "exercises", "squat_reference.png"),
        "primary_joint": "Knee & Hip",
        "target_angle": "100° (Parallel Depth)",
        "guidance_available": True
    },

    "DEADLIFT": {
        "id": "DEADLIFT",
        "name": "Deadlift",
        "display_name": "Conventional Hip-Hinge Deadlift",
        "category": "Posterior Chain",
        "difficulty": "Intermediate",
        "primary_muscles": ["Hamstrings", "Gluteus Maximus", "Erector Spinae"],
        "secondary_muscles": ["Latissimus Dorsi", "Trapezius", "Forearms"],
        "analysis_status": "ACTIVE",
        "status_label": "🟢 LIVE AI ANALYSIS AVAILABLE",
        "status_badge": "ACTIVE AI",
        "status_description": "Real-time hip-hinge tracking, lumbar neutrality monitoring, and lockout extension.",
        "description": "Premier posterior chain movement targeting hamstrings, glutes, and back while enforcing spinal rigidity.",
        "form_reference": os.path.join("assets", "exercises", "deadlift_reference.png"),
        "primary_joint": "Hip & Lumbar Spine",
        "target_angle": "110° (Hip Hinge Apex)",
        "guidance_available": True
    },

    "BICEP_CURL": {
        "id": "BICEP_CURL",
        "name": "Bicep Curl",
        "display_name": "Bilateral Dumbbell Bicep Curl",
        "category": "Upper Body",
        "difficulty": "Beginner",
        "primary_muscles": ["Biceps Brachii", "Brachialis"],
        "secondary_muscles": ["Brachioradialis", "Anterior Deltoid"],
        "analysis_status": "ACTIVE",
        "status_label": "🟢 LIVE AI ANALYSIS AVAILABLE",
        "status_badge": "ACTIVE AI",
        "status_description": "Independent bilateral arm angle tracking, elbow drift detection, and contraction analysis.",
        "description": "Upper-body isolation exercise targeting bicep peak contraction while emphasizing elbow stabilization.",
        "form_reference": os.path.join("assets", "exercises", "bicep_curl_reference.png"),
        "primary_joint": "Elbow Flexion",
        "target_angle": "65° (Peak Contraction)",
        "guidance_available": True
    },

    # ==========================================================================
    # 🔵 GUIDED / LEARNING MODE EXERCISES (Technique Education & Reference)
    # ==========================================================================
    "PUSH_UP": {
        "id": "PUSH_UP",
        "name": "Push-Up",
        "display_name": "Standard Floor Push-Up",
        "category": "Upper Body",
        "difficulty": "Beginner to Intermediate",
        "primary_muscles": ["Pectoralis Major", "Triceps Brachii"],
        "secondary_muscles": ["Anterior Deltoids", "Core (Anti-Extension)", "Serratus Anterior"],
        "analysis_status": "GUIDED",
        "status_label": "🔵 GUIDED TRAINING MODE",
        "status_badge": "GUIDED MODE",
        "status_description": "Reference posture standards, 90° elbow depth cues, and plank alignment guidance.",
        "description": "Foundational horizontal pushing movement building chest, shoulder, and triceps endurance with core tension.",
        "form_reference": os.path.join("assets", "exercises", "push_up_reference.png"),
        "primary_joint": "Elbow & Shoulder",
        "target_angle": "90° (Elbow Depth)",
        "guidance_available": True
    },

    "LUNGE": {
        "id": "LUNGE",
        "name": "Forward Lunge",
        "display_name": "Walking / Forward Lunge",
        "category": "Lower Body",
        "difficulty": "Intermediate",
        "primary_muscles": ["Quadriceps", "Gluteus Medius"],
        "secondary_muscles": ["Hamstrings", "Calves", "Core Stabilizers"],
        "analysis_status": "GUIDED",
        "status_label": "🔵 GUIDED TRAINING MODE",
        "status_badge": "GUIDED MODE",
        "status_description": "Unilateral 90° knee tracking reference, balance guidelines, and vertical shin alignment.",
        "description": "Dynamic unilateral lower-body exercise promoting pelvic stability, leg symmetry, and hip mobility.",
        "form_reference": os.path.join("assets", "exercises", "lunge_reference.png"),
        "primary_joint": "Front & Rear Knee",
        "target_angle": "90° Front / 90° Rear Knee",
        "guidance_available": True
    },

    "PLANK": {
        "id": "PLANK",
        "name": "Forearm Plank",
        "display_name": "Isometric Forearm Plank",
        "category": "Core",
        "difficulty": "Beginner",
        "primary_muscles": ["Rectus Abdominis", "Transverse Abdominis"],
        "secondary_muscles": ["Glutes", "Shoulder Girdle", "Quadriceps"],
        "analysis_status": "GUIDED",
        "status_label": "🔵 GUIDED TRAINING MODE",
        "status_badge": "GUIDED MODE",
        "status_description": "Isometric 180° neutral body line criteria, anti-sagging cues, and pelvic tilt reference.",
        "description": "Essential static core conditioning exercise building deep spinal endurance and anti-extension stability.",
        "form_reference": os.path.join("assets", "exercises", "plank_reference.png"),
        "primary_joint": "Spine & Pelvis (Isometric)",
        "target_angle": "180° Neutral Line",
        "guidance_available": True
    },

    "SHOULDER_PRESS": {
        "id": "SHOULDER_PRESS",
        "name": "Shoulder Press",
        "display_name": "Overhead Barbell / DB Press",
        "category": "Upper Body",
        "difficulty": "Intermediate",
        "primary_muscles": ["Anterior & Lateral Deltoids", "Triceps"],
        "secondary_muscles": ["Upper Trapezius", "Upper Chest", "Core"],
        "analysis_status": "GUIDED",
        "status_label": "🔵 GUIDED TRAINING MODE",
        "status_badge": "GUIDED MODE",
        "status_description": "Vertical press path cues, 170° overhead lockout reference, and ribcage-down posture rules.",
        "description": "Vertical pressing compound movement developing raw shoulder power, triceps lockout, and core bracing.",
        "form_reference": os.path.join("assets", "exercises", "shoulder_press_reference.png"),
        "primary_joint": "Shoulder & Elbow Extension",
        "target_angle": "170° (Overhead Lockout)",
        "guidance_available": True
    }
}


def get_exercise_metadata(exercise_id: str) -> Dict[str, Any]:
    """Retrieves full structured metadata for a given exercise key."""
    key = exercise_id.upper().strip()
    if key in EXERCISE_REGISTRY:
        return EXERCISE_REGISTRY[key]
    return EXERCISE_REGISTRY["SQUAT"]


def get_all_exercises() -> List[Dict[str, Any]]:
    """Returns list of all exercise metadata dictionaries."""
    return list(EXERCISE_REGISTRY.values())


def get_active_exercises() -> List[Dict[str, Any]]:
    """Returns list of exercises currently supported by real-time YOLO AI tracking."""
    return [ex for ex in EXERCISE_REGISTRY.values() if ex["analysis_status"] == "ACTIVE"]


def get_guided_exercises() -> List[Dict[str, Any]]:
    """Returns list of exercises available in Guided / Learning Mode."""
    return [ex for ex in EXERCISE_REGISTRY.values() if ex["analysis_status"] == "GUIDED"]


def is_active_ai_supported(exercise_id: str) -> bool:
    """Returns True if the exercise has full backend YOLO analysis support."""
    meta = get_exercise_metadata(exercise_id)
    return meta.get("analysis_status") == "ACTIVE"


def is_guided_exercise(exercise_id: str) -> bool:
    """Returns True if the exercise is a Guided reference exercise."""
    return not is_active_ai_supported(exercise_id)


def get_exercises_by_category() -> Dict[str, List[Dict[str, Any]]]:
    """Groups all exercises into category buckets."""
    categories: Dict[str, List[Dict[str, Any]]] = {
        "LOWER BODY": [],
        "POSTERIOR CHAIN": [],
        "UPPER BODY": [],
        "CORE": []
    }
    for ex in EXERCISE_REGISTRY.values():
        cat = ex.get("category", "OTHER").upper()
        if cat in categories:
            categories[cat].append(ex)
        else:
            categories.setdefault(cat, []).append(ex)
    return categories
