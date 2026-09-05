"""Personalized Session Improvement Engine & In-Memory Session History Tracker.

Analyzes completed workout telemetry to generate verified strengths, targeted improvement areas,
and next-session goals. Provides lightweight in-memory session comparison across workouts.
"""

from typing import Dict, Any, List, Optional
import time
from datetime import datetime


def generate_session_insights(
    exercise_name: str,
    stats: Optional[Dict[str, Any]] = None,
    duration_seconds: int = 0
) -> Dict[str, Any]:
    """
    Analyzes verified telemetry from a completed session to generate actionable,
    educational coaching insights without modifying any backend algorithms.
    """
    stats = stats or {}
    reps = stats.get("clean_reps", 0)
    total = stats.get("total_attempts", 0)
    acc = int(stats.get("accuracy", 100))
    failed_depth = stats.get("failed_depth", 0)
    failed_sitting = stats.get("failed_sitting", 0)
    posture_warnings = stats.get("posture_warnings", 0)
    ex = exercise_name.upper().strip()

    # Determine Performance Tier
    if acc >= 90:
        tier = "EXCELLENT"
        tier_badge = "🟢 EXCELLENT SESSION"
        tier_summary = "Outstanding movement quality and postural consistency."
    elif acc >= 75:
        tier = "GOOD"
        tier_badge = "🔵 GOOD SESSION"
        tier_summary = "Strong overall mechanics with minor opportunities for refinement."
    elif acc >= 50:
        tier = "NEEDS_IMPROVEMENT"
        tier_badge = "🟡 NEEDS IMPROVEMENT"
        tier_summary = "Technique requires conscious adjustment to ensure safe movement patterns."
    else:
        tier = "FORM_CORRECTION"
        tier_badge = "🔴 FORM CORRECTION REQUIRED"
        tier_summary = "High rate of biomechanical faults detected; slow down and prioritize technique."

    # Identify Strengths
    strengths: List[str] = []
    if acc >= 90:
        strengths.append(f"Exceptional form precision ({acc}% session accuracy).")
    if reps >= 5:
        strengths.append(f"Completed {reps} clean, validated repetitions.")
    if failed_sitting == 0 and total > 0:
        strengths.append("Maintained continuous kinetic tension without passive resting.")
    if failed_depth == 0 and reps > 0:
        strengths.append("Full biomechanical depth achieved on all validated reps.")
    if posture_warnings == 0 and total > 0:
        if ex == "BICEP_CURL":
            strengths.append("Strict elbow stabilization; elbows remained locked to ribcage.")
        else:
            strengths.append("Rigid spinal neutrality and upright posture preserved throughout.")

    if not strengths:
        strengths.append("Successfully initiated and completed computer vision tracking session.")

    # Identify Improvement Opportunities
    improvements: List[str] = []
    if failed_depth > 0:
        improvements.append(f"Depth Control: Address {failed_depth} incomplete repetitions by lowering fully to parallel.")
    if posture_warnings > 0:
        if ex == "BICEP_CURL":
            improvements.append(f"Elbow Stability: Correct {posture_warnings} unpinned elbow warnings; lock elbows to ribcage.")
        else:
            improvements.append(f"Spinal Alignment: Correct {posture_warnings} torso inclination cues; brace abdominal wall.")
    if failed_sitting > 0:
        improvements.append(f"Active Tension: Eliminate {failed_sitting} chair resting events; maintain quad engagement.")
    if reps == 0 and total > 0:
        improvements.append("Pacing: Slow down movement cadence and focus on deliberate joint control.")

    if not improvements:
        improvements.append("Maintain current movement consistency across higher volume sets.")

    # Determine Primary Focus
    if failed_depth >= max(posture_warnings, failed_sitting) and failed_depth > 0:
        primary_focus = "DEPTH CONTROL"
        recommendation = "Practice a 2-second controlled descent and achieve full parallel crease before driving up."
    elif posture_warnings >= max(failed_depth, failed_sitting) and posture_warnings > 0:
        if ex == "BICEP_CURL":
            primary_focus = "ELBOW STABILITY"
            recommendation = "Anchor elbows firmly against your ribcage to isolate biceps and eliminate front deltoid swing."
        else:
            primary_focus = "SPINAL ALIGNMENT"
            recommendation = "Elevate chest, pack lats, and resist excessive forward torso inclination under fatigue."
    elif failed_sitting > 0:
        primary_focus = "ACTIVE TENSION"
        recommendation = "Perform touch-and-go repetitions; do not relax stabilizing musculature at the bottom."
    else:
        primary_focus = "MOVEMENT CONSISTENCY"
        recommendation = "Preserve current alignment and lock in identical cadence across all repetitions."

    # Next Session Goal
    if acc >= 90:
        next_session_goal = "Maintain form score above 90% while progressively challenging session volume."
    elif acc >= 75:
        next_session_goal = f"Target 90%+ form score by focusing specifically on {primary_focus.lower()}."
    else:
        next_session_goal = "Reduce movement tempo by 50% and prioritize correct posture over repetition speed."

    # Format Session Duration
    mins = duration_seconds // 60
    secs = duration_seconds % 60
    duration_str = f"{mins:02d}:{secs:02d}"

    return {
        "exercise": ex,
        "clean_reps": reps,
        "total_attempts": total,
        "accuracy": acc,
        "duration_seconds": duration_seconds,
        "duration_str": duration_str,
        "performance_tier": tier,
        "tier_badge": tier_badge,
        "tier_summary": tier_summary,
        "strengths": strengths,
        "improvements": improvements,
        "primary_focus": primary_focus,
        "recommendation": recommendation,
        "next_session_goal": next_session_goal
    }


class SessionHistoryTracker:
    """In-memory session history tracker enabling runtime comparison without external database."""

    _instance: Optional["SessionHistoryTracker"] = None

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    @classmethod
    def get_instance(cls) -> "SessionHistoryTracker":
        if cls._instance is None:
            cls._instance = SessionHistoryTracker()
        return cls._instance

    def record_session(
        self,
        exercise_name: str,
        stats: Dict[str, Any],
        duration_seconds: int = 0
    ) -> Dict[str, Any]:
        """Calculates insights and appends to in-memory session log."""
        insights = generate_session_insights(exercise_name, stats, duration_seconds)
        insights["timestamp"] = datetime.now().strftime("%H:%M:%S")
        self.history.append(insights)
        return insights

    def get_recent_comparison(self, exercise_name: str) -> Optional[Dict[str, Any]]:
        """
        Compares the most recent session with previous session of the same exercise.
        Returns None if fewer than 2 sessions exist for this exercise.
        """
        ex = exercise_name.upper().strip()
        matches = [s for s in self.history if s.get("exercise") == ex]
        if len(matches) < 2:
            return None

        curr = matches[-1]
        prev = matches[-2]

        curr_acc = curr.get("accuracy", 100)
        prev_acc = prev.get("accuracy", 100)
        delta_acc = curr_acc - prev_acc

        if delta_acc > 0:
            trend_icon = "↑"
            trend_text = f"+{delta_acc}% Form Quality Improvement"
            trend_tier = "IMPROVED"
        elif delta_acc < 0:
            trend_icon = "↓"
            trend_text = f"{delta_acc}% Form Quality Shift"
            trend_tier = "DECLINED"
        else:
            trend_icon = "→"
            trend_text = "Consistent Performance (0% delta)"
            trend_tier = "STABLE"

        return {
            "current_accuracy": curr_acc,
            "previous_accuracy": prev_acc,
            "delta_accuracy": delta_acc,
            "trend_icon": trend_icon,
            "trend_text": trend_text,
            "trend_tier": trend_tier,
            "previous_reps": prev.get("clean_reps", 0),
            "current_reps": curr.get("clean_reps", 0)
        }

    def get_recent_sessions(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Returns the most recent completed sessions."""
        return self.history[-limit:]

    def clear(self):
        """Clears in-memory session history."""
        self.history.clear()
