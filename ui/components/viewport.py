"""Viewport component displaying the video stream and live coach feedback banner."""

from typing import Optional
import customtkinter as ctk
from ui import theme


class ViewportFrame(ctk.CTkFrame):
    """Main view area with video feed canvas and live coach status bar."""

    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=15, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Video Viewport
        self.video_label = ctk.CTkLabel(self, text="", corner_radius=12)
        self.video_label.grid(row=0, column=0, padx=15, pady=(15, 10), sticky="nsew")

        # Bottom Coach Feedback Toast
        self.status_bar = ctk.CTkFrame(self, height=55, corner_radius=10, fg_color=theme.COLOR_STATUS_BG)
        self.status_bar.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="ew")
        self.status_bar.grid_columnconfigure(1, weight=1)

        self.feedback_title = ctk.CTkLabel(
            self.status_bar,
            text="LIVE COACH:",
            font=ctk.CTkFont(size=theme.FONT_COACH_TAG[1], weight=theme.FONT_COACH_TAG[2]),
            text_color=theme.COLOR_MUTED
        )
        self.feedback_title.grid(row=0, column=0, padx=(15, 5), pady=12)

        self.feedback_val = ctk.CTkLabel(
            self.status_bar,
            text="Select exercise and click START WORKOUT",
            font=ctk.CTkFont(size=theme.FONT_COACH_MESSAGE[1], weight=theme.FONT_COACH_MESSAGE[2]),
            text_color=theme.COLOR_ACCENT
        )
        self.feedback_val.grid(row=0, column=1, padx=5, pady=12, sticky="w")

    def update_frame(self, ctk_img: ctk.CTkImage):
        """Updates the video display image."""
        self.video_label.configure(image=ctk_img)

    def update_feedback(self, message: str, color: Optional[str] = None):
        """Updates the coach banner feedback message and text color."""
        text_color = color or theme.COLOR_ACCENT
        self.feedback_val.configure(text=message, text_color=text_color)
