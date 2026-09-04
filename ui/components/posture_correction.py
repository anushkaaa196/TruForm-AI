"""AI Posture Correction Console Component.

Displays real-time categorized posture status, current AI observation, actionable coaching cue,
and priority level directly below the live video stream.
"""

from typing import Optional, Dict, Any
import customtkinter as ctk
from ui import theme
from core.exercise_guidance import classify_posture_feedback


class PostureCorrectionCard(ctk.CTkFrame):
    """High-contrast real-time posture correction console."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            corner_radius=12,
            fg_color=theme.COLOR_STATUS_BG,
            border_width=1,
            border_color=theme.COLOR_BORDER,
            **kwargs
        )
        self.grid_columnconfigure(1, weight=1)

        # ----------------------------------------------------------------------
        # Left: Severity Indicator Strip
        # ----------------------------------------------------------------------
        self.status_strip = ctk.CTkFrame(
            self,
            width=5,
            corner_radius=3,
            fg_color=theme.COLOR_ACCENT
        )
        self.status_strip.grid(row=0, column=0, rowspan=2, padx=(12, 10), pady=8, sticky="ns")

        # ----------------------------------------------------------------------
        # Top Row: Category Tag, Observation, and Priority Badge
        # ----------------------------------------------------------------------
        self.top_row = ctk.CTkFrame(self, fg_color="transparent")
        self.top_row.grid(row=0, column=1, padx=(0, 12), pady=(8, 2), sticky="ew")
        self.top_row.grid_columnconfigure(1, weight=1)

        # Category Pill
        self.category_pill = ctk.CTkLabel(
            self.top_row,
            text="● AI STANDBY",
            font=ctk.CTkFont(size=theme.FONT_BADGE[1], weight=theme.FONT_BADGE[2]),
            fg_color=theme.COLOR_ACCENT_MUTED,
            text_color=theme.COLOR_ACCENT,
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.category_pill.grid(row=0, column=0, sticky="w")

        # Live AI Observation
        self.observation_lbl = ctk.CTkLabel(
            self.top_row,
            text="Select exercise and click START WORKOUT to initialize AI tracking",
            font=ctk.CTkFont(size=theme.FONT_COACH_MESSAGE[1], weight=theme.FONT_COACH_MESSAGE[2]),
            text_color=theme.COLOR_TEXT_PRIMARY,
            anchor="w"
        )
        self.observation_lbl.grid(row=0, column=1, padx=(10, 8), sticky="w")

        # Priority Badge
        self.priority_badge = ctk.CTkLabel(
            self.top_row,
            text="PRIORITY: LOW",
            font=ctk.CTkFont(size=theme.FONT_BADGE[1], weight=theme.FONT_BADGE[2]),
            fg_color=theme.COLOR_CARD_BG,
            text_color=theme.COLOR_TEXT_MUTED,
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.priority_badge.grid(row=0, column=2, sticky="e")

        # ----------------------------------------------------------------------
        # Bottom Row: Actionable Coaching Cue & Next Rep Hint
        # ----------------------------------------------------------------------
        self.bottom_row = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_row.grid(row=1, column=1, padx=(0, 12), pady=(0, 8), sticky="ew")
        self.bottom_row.grid_columnconfigure(1, weight=1)

        self.action_tag = ctk.CTkLabel(
            self.bottom_row,
            text="COACHING ACTION:",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_TEXT_MUTED
        )
        self.action_tag.grid(row=0, column=0, sticky="w")

        self.action_lbl = ctk.CTkLabel(
            self.bottom_row,
            text="Maintain a neutral spine and controlled, rhythmic cadence.",
            font=ctk.CTkFont(size=theme.FONT_SUBTITLE[1]),
            text_color=theme.COLOR_ACCENT,
            anchor="w"
        )
        self.action_lbl.grid(row=0, column=1, padx=(6, 8), sticky="w")

        self.next_rep_pill = ctk.CTkLabel(
            self.bottom_row,
            text="NEXT REP: Controlled Movement",
            font=ctk.CTkFont(size=9, weight="bold"),
            fg_color=theme.COLOR_CARD_BG,
            text_color=theme.COLOR_TEXT_SECONDARY,
            corner_radius=4,
            padx=6,
            pady=1
        )
        self.next_rep_pill.grid(row=0, column=2, sticky="e")

    def update_correction(
        self,
        exercise_name: str,
        feedback_msg: str,
        feedback_color: str
    ) -> Dict[str, Any]:
        """
        Updates the posture correction console using categorized feedback.
        Returns the structured classification dictionary for synchronization with other components.
        """
        data = classify_posture_feedback(exercise_name, feedback_msg, feedback_color)

        cat = data["category"]
        if cat == "CORRECT":
            accent = theme.COLOR_SUCCESS
            badge_bg = theme.COLOR_SUCCESS_MUTED
            pri_bg = theme.COLOR_SUCCESS_MUTED
            pri_color = theme.COLOR_SUCCESS
        elif cat == "CRITICAL":
            accent = theme.COLOR_ALERT
            badge_bg = theme.COLOR_ALERT_MUTED
            pri_bg = theme.COLOR_ALERT_MUTED
            pri_color = theme.COLOR_ALERT
        elif cat == "WARNING":
            accent = theme.COLOR_WARN
            badge_bg = theme.COLOR_WARN_MUTED
            pri_bg = theme.COLOR_WARN_MUTED
            pri_color = theme.COLOR_WARN
        else:
            accent = theme.COLOR_ACCENT
            badge_bg = theme.COLOR_ACCENT_MUTED
            pri_bg = theme.COLOR_CARD_BG
            pri_color = theme.COLOR_TEXT_MUTED

        # Update Visuals
        self.status_strip.configure(fg_color=accent)
        self.category_pill.configure(text=f"● {data['status_label']}", text_color=accent, fg_color=badge_bg)
        self.observation_lbl.configure(text=data["observation"])
        self.action_lbl.configure(text=data["action"], text_color=accent)
        self.priority_badge.configure(text=f"PRIORITY: {data['priority']}", text_color=pri_color, fg_color=pri_bg)
        self.next_rep_pill.configure(text=f"NEXT REP: {data['next_rep_focus'][:28]}...")
        self.configure(border_color=accent)

        return data

    def reset(self):
        """Resets console to initial standby state."""
        self.status_strip.configure(fg_color=theme.COLOR_ACCENT)
        self.category_pill.configure(text="● AI STANDBY", text_color=theme.COLOR_ACCENT, fg_color=theme.COLOR_ACCENT_MUTED)
        self.observation_lbl.configure(text="Select exercise and click START WORKOUT to initialize AI tracking")
        self.action_lbl.configure(text="Maintain a neutral spine and controlled, rhythmic cadence.", text_color=theme.COLOR_ACCENT)
        self.priority_badge.configure(text="PRIORITY: LOW", text_color=theme.COLOR_TEXT_MUTED, fg_color=theme.COLOR_CARD_BG)
        self.next_rep_pill.configure(text="NEXT REP: Controlled Movement")
        self.configure(border_color=theme.COLOR_BORDER)
