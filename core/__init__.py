"""Core biomechanics, math, and filtering package."""

from .filters import LowPassFilter
from .geometry import calculate_angle, extract_valid_profile, extract_exercise_data
from .biomechanics import classify_sitting, check_hands_up_gesture
from .exercise_guidance import (
    get_exercise_guidance,
    get_all_supported_exercises,
    get_roadmap_exercises,
    find_guidance_highlight,
    classify_posture_feedback
)
from .exercise_registry import (
    EXERCISE_REGISTRY,
    get_exercise_metadata,
    get_all_exercises,
    get_active_exercises,
    get_guided_exercises,
    is_active_ai_supported,
    get_exercises_by_category
)
from .session_insights import (
    generate_session_insights,
    SessionHistoryTracker
)
from .rep_analysis import analyze_repetition
from .rep_history import RepHistoryTracker
from .personalized_coach import generate_personalized_plan
from .session_goals import get_exercise_goal, evaluate_goal_progress
from .form_comparison import get_form_comparison
from .progress_intelligence import ProgressIntelligenceTracker
from .movement_phases import MovementPhaseEngine, get_movement_phase_engine
from .movement_stability import MovementStabilityEngine, get_movement_stability_engine
from .fatigue_intelligence import estimate_form_fatigue
from .risk_intelligence import evaluate_movement_risk
from .adaptive_coaching import get_adaptive_coaching
from .readiness_intelligence import evaluate_workout_readiness
from .recovery_recommendations import get_recovery_recommendations
from .performance_trends import analyze_performance_trends

__all__ = [
    "LowPassFilter",
    "calculate_angle",
    "extract_valid_profile",
    "extract_exercise_data",
    "classify_sitting",
    "check_hands_up_gesture",
    "get_exercise_guidance",
    "get_all_supported_exercises",
    "get_roadmap_exercises",
    "find_guidance_highlight",
    "classify_posture_feedback",
    "EXERCISE_REGISTRY",
    "get_exercise_metadata",
    "get_all_exercises",
    "get_active_exercises",
    "get_guided_exercises",
    "is_active_ai_supported",
    "get_exercises_by_category",
    "generate_session_insights",
    "SessionHistoryTracker",
    "analyze_repetition",
    "RepHistoryTracker",
    "generate_personalized_plan",
    "get_exercise_goal",
    "evaluate_goal_progress",
    "get_form_comparison",
    "ProgressIntelligenceTracker",
    "MovementPhaseEngine",
    "get_movement_phase_engine",
    "MovementStabilityEngine",
    "get_movement_stability_engine",
    "estimate_form_fatigue",
    "evaluate_movement_risk",
    "get_adaptive_coaching",
    "evaluate_workout_readiness",
    "get_recovery_recommendations",
    "analyze_performance_trends"
]


