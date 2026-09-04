import os
import sys
from pathlib import Path

# Add workspace root to sys.path
root_dir = str(Path(__file__).resolve().parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from PIL import Image
import customtkinter as ctk

from core.exercise_guidance import (
    classify_posture_feedback,
    get_exercise_guidance,
    get_all_supported_exercises
)
from ui.components import (
    PostureCorrectionCard,
    BodyFocusCard,
    SmartCoachCard,
    LiveAnalyticsFrame
)
from ui.app import AIWorkoutUI


def run_phase3_tests():
    print("=== 1. Testing classify_posture_feedback ===")
    # A. Optimal Form
    c_opt = classify_posture_feedback("SQUAT", "Clean Rep! (100 deg)", "#00E676")
    assert c_opt["category"] == "CORRECT", f"Expected CORRECT, got {c_opt['category']}"
    assert c_opt["status_label"] == "OPTIMAL FORM"
    assert c_opt["priority"] == "LOW"
    assert c_opt["body_focus"] == "FULL_BODY"
    print("Optimal form classification verified.")

    # B. Knee Valgus Warning
    c_knee = classify_posture_feedback("SQUAT", "Knees collapsing inward", "#FF9100")
    assert c_knee["category"] == "WARNING"
    assert c_knee["body_focus"] == "KNEES"
    assert "KNEE" in c_knee["focus_label"]
    assert "toes" in c_knee["action"].lower()
    print("Knee warning classification verified.")

    # C. Torso Lean Warning
    c_torso = classify_posture_feedback("DEADLIFT", "Torso leaning too far forward", "#FF9100")
    assert c_torso["category"] == "WARNING"
    assert c_torso["body_focus"] == "SPINE"
    assert "chest" in c_torso["action"].lower()
    print("Torso lean classification verified.")

    # D. Incomplete Depth
    c_depth = classify_posture_feedback("SQUAT", "Incomplete depth - go deeper", "#FF9100")
    assert c_depth["body_focus"] == "HIPS"
    print("Depth classification verified.")

    # E. Elbow Sway
    c_elbow = classify_posture_feedback("BICEP_CURL", "Keep elbows pinned at sides", "#FF9100")
    assert c_elbow["body_focus"] == "ELBOWS"
    print("Elbow stability classification verified.")

    # F. Critical Fault
    c_crit = classify_posture_feedback("SQUAT", "Rep Disqualified: Sitting on chair", "#FF1744")
    assert c_crit["category"] == "CRITICAL"
    assert c_crit["priority"] == "HIGH"
    assert c_crit["status_label"] == "CRITICAL CORRECTION"
    print("Critical fault classification verified.")

    print("\n=== 2. Testing Component Instantiations ===")
    root = ctk.CTk()
    root.withdraw()  # headless

    # Test PostureCorrectionCard
    p_card = PostureCorrectionCard(root)
    p_data = p_card.update_correction("SQUAT", "Knees collapsing inward", "#FF9100")
    assert p_data["body_focus"] == "KNEES"
    p_card.reset()
    print("PostureCorrectionCard verified.")

    # Test BodyFocusCard
    b_card = BodyFocusCard(root)
    b_card.set_focus("KNEES", "KNEE ALIGNMENT — TRACK OVER TOES", "WARNING")
    assert b_card.focus_label.cget("text") == "KNEE ALIGNMENT — TRACK OVER TOES"
    b_card.reset()
    print("BodyFocusCard verified.")

    # Test SmartCoachCard
    s_card = SmartCoachCard(root)
    s_card.update_coach(p_data)
    assert len(s_card.what_lbl.cget("text")) > 0
    assert len(s_card.why_lbl.cget("text")) > 0
    s_card.reset()
    print("SmartCoachCard verified.")

    # Test LiveAnalyticsFrame
    a_frame = LiveAnalyticsFrame(root)
    stats = {
        "clean_reps": 8,
        "total_attempts": 10,
        "accuracy": 80,
        "failed_depth": 1,
        "failed_sitting": 0,
        "posture_warnings": 1
    }
    a_frame.update_analytics(stats)
    assert a_frame.score_val.cget("text") == "80%"
    assert a_frame.valid_reps_lbl.cget("text") == "8"
    assert "80%" in a_frame.success_rate_lbl.cget("text")
    assert len(a_frame.trend_history) >= 2
    a_frame.reset_analytics()
    assert a_frame.score_val.cget("text") == "100%"
    assert a_frame.valid_reps_lbl.cget("text") == "0"
    print("LiveAnalyticsFrame verified.")

    root.destroy()

    print("\n=== 3. Testing Full AIWorkoutUI Application Integration ===")
    app = AIWorkoutUI()
    assert hasattr(app, "sidebar") and app.sidebar is not None
    assert hasattr(app, "viewport") and app.viewport is not None
    assert hasattr(app, "form_guide") and app.form_guide is not None
    assert hasattr(app, "analytics") and app.analytics is not None

    # Test Exercise Switching
    app._on_exercise_selected("DEADLIFT")
    assert app.engine.current_exercise == "DEADLIFT"
    assert app.viewport.exercise_badge.cget("text") == "DEADLIFT"
    assert app.form_guide.current_exercise == "DEADLIFT"
    print("Exercise switch to DEADLIFT verified.")

    app._on_exercise_selected("BICEP_CURL")
    assert app.engine.current_exercise == "BICEP_CURL"
    print("Exercise switch to BICEP_CURL verified.")

    # Test Live Frame Update with Full Telemetry
    pil_dummy = Image.new("RGB", (720, 480), (15, 25, 35))
    ctk_dummy = ctk.CTkImage(light_image=pil_dummy, dark_image=pil_dummy, size=(720, 480))
    app._apply_ui_updates(
        ctk_dummy,
        5,
        85,
        "Knees collapsing inward",
        "#FF9100",
        stats={
            "clean_reps": 5,
            "total_attempts": 6,
            "accuracy": 85,
            "failed_depth": 1,
            "failed_sitting": 0,
            "posture_warnings": 1
        }
    )
    assert app.analytics.score_val.cget("text") == "85%"
    assert app.analytics.valid_reps_lbl.cget("text") == "5"
    assert "KNEE" in app.form_guide.body_focus_card.focus_label.cget("text")
    print("Full telemetry pipeline update verified.")

    # Test Reset Metrics
    app._on_reset_metrics()
    assert app.analytics.score_val.cget("text") == "100%"
    assert app.analytics.valid_reps_lbl.cget("text") == "0"
    print("Full application reset verified.")

    # Test Report Export Compatibility
    exported_file = app.engine.export_report()
    assert os.path.exists(exported_file), f"Exported report missing: {exported_file}"
    print(f"Phase 1 report export verified: {exported_file}")

    # Clean shutdown
    app.destroy()
    print("\n=== ALL PHASE 3 VERIFICATION TESTS PASSED SUCCESSFULLY! ===")


if __name__ == "__main__":
    run_phase3_tests()
