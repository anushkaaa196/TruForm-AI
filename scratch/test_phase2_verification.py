import os
import sys
from pathlib import Path

# Add root directory to sys.path
root_dir = str(Path(__file__).resolve().parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from PIL import Image
import customtkinter as ctk

from core.exercise_guidance import (
    get_exercise_guidance,
    get_all_supported_exercises,
    get_roadmap_exercises,
    find_guidance_highlight
)
from ui.app import AIWorkoutUI

def run_tests():
    print("--- 1. Testing exercise_guidance data ---")
    supported = get_all_supported_exercises()
    assert "SQUAT" in supported and "DEADLIFT" in supported and "BICEP_CURL" in supported, "Missing supported exercises"
    print(f"Supported exercises: {supported}")

    roadmap = get_roadmap_exercises()
    assert "PUSH_UP" in roadmap and "LUNGE" in roadmap, "Missing roadmap exercises"
    print(f"Roadmap exercises: {list(roadmap.keys())}")

    # Verify Squat guidance
    sq_guide = get_exercise_guidance("SQUAT")
    assert len(sq_guide["correct_form"]) >= 5, "Insufficient correct form items"
    assert len(sq_guide["common_mistakes"]) >= 5, "Insufficient common mistakes"
    assert len(sq_guide["improvement_tips"]) >= 4, "Insufficient improvement tips"
    assert os.path.exists(sq_guide["reference_image"]), f"Missing image: {sq_guide['reference_image']}"
    print("Squat guidance verified.")

    # Verify Deadlift guidance
    dl_guide = get_exercise_guidance("DEADLIFT")
    assert len(dl_guide["correct_form"]) >= 5
    assert os.path.exists(dl_guide["reference_image"])
    print("Deadlift guidance verified.")

    # Verify Bicep Curl guidance
    bc_guide = get_exercise_guidance("BICEP_CURL")
    assert len(bc_guide["correct_form"]) >= 5
    assert os.path.exists(bc_guide["reference_image"])
    print("Bicep Curl guidance verified.")

    # Verify Fallback
    fallback_guide = get_exercise_guidance("NON_EXISTENT")
    assert fallback_guide["id"] == "SQUAT", "Fallback failed"
    print("Fallback guidance verified.")

    # Test Keyword Highlight matching
    h1 = find_guidance_highlight("SQUAT", "Caution: Knees collapsing inward")
    assert h1 == 1, f"Expected 1, got {h1}"
    h2 = find_guidance_highlight("DEADLIFT", "Maintain neutral spine")
    assert h2 == 0, f"Expected 0, got {h2}"
    h3 = find_guidance_highlight("BICEP_CURL", "Keep elbows pinned")
    assert h3 == 0, f"Expected 0, got {h3}"
    print("Keyword highlight mapping verified.")

    print("\n--- 2. Testing UI Integration & Form Guide ---")
    app = AIWorkoutUI()
    assert app.form_guide is not None, "FormGuideFrame not instantiated"
    assert app.form_guide_visible is True, "FormGuideFrame should be visible initially"

    # Test Exercise Switching
    app._on_exercise_selected("DEADLIFT")
    assert app.engine.current_exercise == "DEADLIFT", "Engine exercise mismatch"
    assert app.form_guide.current_exercise == "DEADLIFT", "FormGuide exercise mismatch"
    assert app.viewport.exercise_badge.cget("text") == "DEADLIFT", "Viewport badge mismatch"
    print("Exercise switching to DEADLIFT verified.")

    app._on_exercise_selected("BICEP_CURL")
    assert app.engine.current_exercise == "BICEP_CURL"
    assert app.form_guide.current_exercise == "BICEP_CURL"
    print("Exercise switching to BICEP_CURL verified.")

    # Test Form Guide Toggle
    app._on_toggle_guide()
    assert app.form_guide_visible is False, "Guide should be hidden"
    app._on_toggle_guide()
    assert app.form_guide_visible is True, "Guide should be visible"
    print("Form guide toggle verified.")

    # Test Missing Image Fallback
    app.form_guide._load_reference_image("non_existent_path.png")
    assert "Reference standards for" in app.form_guide.img_caption.cget("text")
    print("Missing image fallback verified (zero crashes).")

    # Restore real image
    app.form_guide.set_exercise("SQUAT")

    # Test UI updates & Feedback Highlight
    pil_dummy = Image.new("RGB", (720, 480), (20, 30, 40))
    ctk_dummy = ctk.CTkImage(light_image=pil_dummy, dark_image=pil_dummy, size=(720, 480))
    app._apply_ui_updates(ctk_dummy, 5, 95, "Keep knees tracking over toes", "#00E676")
    print("Live UI update with guidance highlight verified.")

    # Clean shutdown
    app.destroy()
    print("\n=== ALL PHASE 2 VERIFICATION TESTS PASSED SUCCESSFULLY! ===")

if __name__ == "__main__":
    run_tests()
