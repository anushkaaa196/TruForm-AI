"""Smart AI Coach & Next Rep Focus Component.

Provides contextual educational guidance: current status, actionable instructions,
biomechanical rationale, and tactical next-rep focus cues.
"""

from typing import Dict, Any, Optional
import customtkinter as ctk
from ui import theme


class SmartCoachCard(ctk.CTkFrame):
    """Educational AI coach panel delivering real-time movement guidance."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            corner_radius=10,
            fg_color=theme.COLOR_CARD_BG,
            border_width=1,
            border_color=theme.COLOR_BORDER,
            **kwargs
        )
        self.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------------------------
        # Header
        # ----------------------------------------------------------------------
        self.header_row = ctk.CTkFrame(self, fg_color="transparent")
        self.header_row.pack(fill="x", padx=12, pady=(8, 4))

        self.title_lbl = ctk.CTkLabel(
            self.header_row,
            text="SMART AI COACH",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_ACCENT
        )
        self.title_lbl.pack(side="left")

        self.status_badge = ctk.CTkLabel(
            self.header_row,
            text="ANALYZING",
            font=ctk.CTkFont(size=8, weight="bold"),
            fg_color=theme.COLOR_ACCENT_MUTED,
            text_color=theme.COLOR_ACCENT,
            corner_radius=4,
            padx=6,
            pady=1
        )
        self.status_badge.pack(side="right")

        # ----------------------------------------------------------------------
        # 1. Current Status & What To Do
        # ----------------------------------------------------------------------
        self.action_card = ctk.CTkFrame(
            self,
            corner_radius=6,
            fg_color=theme.COLOR_CARD_INNER,
            border_width=1,
            border_color=theme.COLOR_BORDER
        )
        self.action_card.pack(fill="x", padx=10, pady=3)

        self.what_title = ctk.CTkLabel(
            self.action_card,
            text="ACTIONABLE INSTRUCTION",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color=theme.COLOR_ACCENT
        )
        self.what_title.pack(anchor="w", padx=8, pady=(4, 1))

        self.what_lbl = ctk.CTkLabel(
            self.action_card,
            text="Replicate current movement pattern on every repetition.",
            font=ctk.CTkFont(size=10),
            text_color=theme.COLOR_TEXT_PRIMARY,
            wraplength=270,
            justify="left"
        )
        self.what_lbl.pack(anchor="w", padx=8, pady=(0, 6))

        # ----------------------------------------------------------------------
        # 2. Why It Matters (Biomechanical Rationale)
        # ----------------------------------------------------------------------
        self.why_card = ctk.CTkFrame(
            self,
            corner_radius=6,
            fg_color=theme.COLOR_CARD_INNER,
            border_width=1,
            border_color=theme.COLOR_BORDER
        )
        self.why_card.pack(fill="x", padx=10, pady=3)

        self.why_title = ctk.CTkLabel(
            self.why_card,
            text="BIOMECHANICAL RATIONALE",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color=theme.COLOR_TEXT_MUTED
        )
        self.why_title.pack(anchor="w", padx=8, pady=(4, 1))

        self.why_lbl = ctk.CTkLabel(
            self.why_card,
            text="Postural consistency builds neuromuscular memory and injury resilience.",
            font=ctk.CTkFont(size=10),
            text_color=theme.COLOR_TEXT_SECONDARY,
            wraplength=270,
            justify="left"
        )
        self.why_lbl.pack(anchor="w", padx=8, pady=(0, 6))

        # ----------------------------------------------------------------------
        # 3. Next Rep Focus
        # ----------------------------------------------------------------------
        self.next_card = ctk.CTkFrame(
            self,
            corner_radius=6,
            fg_color=theme.COLOR_CARD_INNER,
            border_width=1,
            border_color=theme.COLOR_ACCENT_MUTED
        )
        self.next_card.pack(fill="x", padx=10, pady=(3, 8))

        self.next_title = ctk.CTkLabel(
            self.next_card,
            text="NEXT REP FOCUS",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color=theme.COLOR_SUCCESS
        )
        self.next_title.pack(anchor="w", padx=8, pady=(4, 1))

        self.next_lbl = ctk.CTkLabel(
            self.next_card,
            text="Maintain your current form. Focus on controlled, rhythmic movement.",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color=theme.COLOR_TEXT_PRIMARY,
            wraplength=270,
            justify="left"
        )
        self.next_lbl.pack(anchor="w", padx=8, pady=(0, 6))

    def update_coach(self, data: Dict[str, Any]):
        """Updates coaching guidance from classified feedback data."""
        cat = data.get("category", "CORRECT")
        if cat == "CORRECT":
            color = theme.COLOR_SUCCESS
            badge_bg = theme.COLOR_SUCCESS_MUTED
        elif cat == "CRITICAL":
            color = theme.COLOR_ALERT
            badge_bg = theme.COLOR_ALERT_MUTED
        elif cat == "WARNING":
            color = theme.COLOR_WARN
            badge_bg = theme.COLOR_WARN_MUTED
        else:
            color = theme.COLOR_ACCENT
            badge_bg = theme.COLOR_ACCENT_MUTED

        self.status_badge.configure(text=data.get("status_label", "ACTIVE"), text_color=color, fg_color=badge_bg)
        self.what_lbl.configure(text=data.get("what_to_do", ""))
        self.why_lbl.configure(text=data.get("why_it_matters", ""))
        self.next_lbl.configure(text=data.get("next_rep_focus", ""), text_color=color)

    def reset(self):
        """Resets to baseline coaching state."""
        self.status_badge.configure(text="READY", text_color=theme.COLOR_ACCENT, fg_color=theme.COLOR_ACCENT_MUTED)
        self.what_lbl.configure(text="Replicate current movement pattern on every repetition.")
        self.why_lbl.configure(text="Postural consistency builds neuromuscular memory and injury resilience.")
        self.next_lbl.configure(
            text="Maintain your current form. Focus on controlled, rhythmic movement.",
            text_color=theme.COLOR_TEXT_PRIMARY
        )
