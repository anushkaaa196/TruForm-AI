import sys
from pathlib import Path

# Ensure root workspace directory is in sys.path
_ROOT = str(Path(__file__).resolve().parent.parent)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from typing import Dict, Any
import cv2
import numpy as np
from PIL import Image
import customtkinter as ctk

from config import EXERCISE_CONFIGS
from backend import WorkoutEngine
from ui import theme
from ui.components import SidebarFrame, ViewportFrame


class AIWorkoutUI(ctk.CTk):
    """Main application controller and graphical user interface."""

    def __init__(self):
        super().__init__()

        theme.setup_theme()

        self.title("AI Biomechanics & Posture Analyzer")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        # Configure root layout grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Backend Engine
        self.engine = WorkoutEngine(on_frame_processed=self._on_frame_processed)

        # Subcomponents
        self.sidebar = SidebarFrame(
            self,
            exercise_list=list(EXERCISE_CONFIGS.keys()),
            on_exercise_selected=self._on_exercise_selected,
            on_toggle_session=self._on_toggle_session,
            on_export_report=self._on_export_report,
            on_reset_metrics=self._on_reset_metrics
        )
        self.sidebar.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.viewport = ViewportFrame(self)
        self.viewport.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _on_exercise_selected(self, exercise_name: str):
        """Switches the active exercise and resets telemetry."""
        self.engine.set_exercise(exercise_name)
        self.sidebar.update_stats(0, 100)

    def _on_toggle_session(self):
        """Toggles workout session state between active and stopped."""
        if not self.engine.is_running:
            success = self.engine.start()
            if success:
                self.sidebar.set_session_state(True)
            else:
                self.viewport.update_feedback("Error: Unable to initialize camera.", theme.COLOR_ALERT)
        else:
            self.engine.stop()
            self.sidebar.set_session_state(False)

    def _on_export_report(self):
        """Exports session summary image and displays confirmation toast."""
        filename = self.engine.export_report()
        self.viewport.update_feedback(f"Report exported as {filename}", theme.COLOR_ACCENT)

    def _on_reset_metrics(self):
        """Resets telemetry stats in backend and UI."""
        self.engine.reset_metrics()
        self.sidebar.update_stats(0, 100)

    def _on_frame_processed(
        self,
        frame: np.ndarray,
        feedback_msg: str,
        feedback_color: str,
        stats: Dict[str, Any]
    ):
        """Converts frame to CTkImage in background thread and schedules UI update."""
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img)
        pil_img = pil_img.resize((780, 500))
        ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(780, 500))

        # Schedule thread-safe main loop update
        self.after(
            0,
            self._apply_ui_updates,
            ctk_img,
            stats["clean_reps"],
            stats["accuracy"],
            feedback_msg,
            feedback_color
        )

    def _apply_ui_updates(
        self,
        ctk_img: ctk.CTkImage,
        reps: int,
        acc: int,
        feedback_msg: str,
        feedback_color: str
    ):
        """Applies visual updates strictly on the Tkinter main thread."""
        self.sidebar.update_stats(reps, acc)
        self.viewport.update_frame(ctk_img)
        self.viewport.update_feedback(feedback_msg, feedback_color)

    def on_close(self):
        """Tears down backend engine and closes window safely."""
        self.engine.stop()
        self.destroy()


def run_app():
    """Application runner."""
    app = AIWorkoutUI()
    app.mainloop()


if __name__ == "__main__":
    run_app()
