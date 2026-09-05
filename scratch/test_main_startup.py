"""Test headless startup and layout rendering of main AIWorkoutUI."""
import sys
from pathlib import Path

_ROOT = str(Path(__file__).resolve().parent.parent)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from ui.app import AIWorkoutUI

def test_startup():
    print("Initializing AIWorkoutUI window...")
    app = AIWorkoutUI()
    app.update_idletasks()
    
    # Check that the 4 workout buttons exist and are mapped in the controls frame
    assert app.sidebar.btn_start.winfo_exists()
    assert app.sidebar.btn_stop.winfo_exists()
    assert app.sidebar.btn_report.winfo_exists()
    assert app.sidebar.btn_reset.winfo_exists()

    ctrl_h = app.sidebar.controls_frame.winfo_height()
    print(f"Controls frame rendered successfully with height: {ctrl_h}px")
    assert ctrl_h > 100, f"Controls frame height too small: {ctrl_h}"

    print(f"Button 1: {app.sidebar.btn_start.cget('text')} [State: {app.sidebar.btn_start.cget('state')}]")
    print(f"Button 2: {app.sidebar.btn_stop.cget('text')} [State: {app.sidebar.btn_stop.cget('state')}]")
    print(f"Button 3: {app.sidebar.btn_report.cget('text')} [State: {app.sidebar.btn_report.cget('state')}]")
    print(f"Button 4: {app.sidebar.btn_reset.cget('text')} [State: {app.sidebar.btn_reset.cget('state')}]")

    # Check compact session overview dock and Analytics Hub launcher
    assert app.analytics.winfo_exists()
    assert app.analytics.score_card.winfo_exists()
    assert app.analytics.btn_open_analytics.winfo_exists()
    print("Compact session overview dock verified.")

    # Test opening Analytics Hub from app
    app._open_analytics_hub("OVERVIEW")
    assert app.analytics_hub is not None
    assert app.analytics_hub.winfo_exists()
    print("Analytics Hub opened and verified from main app.")
    app.analytics_hub.destroy()

    # Test opening Nutrition Dashboard from app (Phase 7C)
    app._open_nutrition_dashboard()
    assert app.nutrition_dashboard is not None
    assert app.nutrition_dashboard.winfo_exists()
    print("Phase 7C Nutrition Dashboard opened and verified from main app.")
    app.nutrition_dashboard.destroy()

    app.destroy()
    print("Application closed cleanly.")

if __name__ == "__main__":
    test_startup()
