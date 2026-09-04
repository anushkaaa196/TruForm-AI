"""AI Camera Readiness & Pre-Workout Calibration Card Component.

Displays optical checklist, room space guidelines, and a quick onboarding flow
in the video viewport before starting real-time computer vision tracking.
"""

from typing import Callable, Optional
import customtkinter as ctk
from ui import theme


class ReadinessCheckCard(ctk.CTkFrame):
    """High-contrast futuristic onboarding and readiness checklist."""

    def __init__(self, master, on_start: Optional[Callable[[], None]] = None, **kwargs):
        super().__init__(
            master,
            corner_radius=12,
            fg_color=theme.COLOR_CARD_INNER,
            border_width=1,
            border_color=theme.COLOR_BORDER,
            **kwargs
        )
        self.on_start = on_start
        self.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------------------------
        # Header
        # ----------------------------------------------------------------------
        self.title_row = ctk.CTkFrame(self, fg_color="transparent")
        self.title_row.pack(fill="x", padx=20, pady=(16, 6))

        self.title_lbl = ctk.CTkLabel(
            self.title_row,
            text="⚡ AI CAMERA READINESS & CALIBRATION",
            font=ctk.CTkFont(size=theme.FONT_SECTION_HEADER[1], weight=theme.FONT_SECTION_HEADER[2]),
            text_color=theme.COLOR_TEXT_PRIMARY
        )
        self.title_lbl.pack(side="left")

        self.ready_badge = ctk.CTkLabel(
            self.title_row,
            text="SYSTEM ONLINE",
            font=ctk.CTkFont(size=theme.FONT_BADGE[1], weight=theme.FONT_BADGE[2]),
            fg_color=theme.COLOR_SUCCESS_MUTED,
            text_color=theme.COLOR_SUCCESS,
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.ready_badge.pack(side="right")

        # ----------------------------------------------------------------------
        # 4-Item Telemetry Checklist
        # ----------------------------------------------------------------------
        self.checklist_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.checklist_frame.pack(fill="x", padx=20, pady=8)
        self.checklist_frame.grid_columnconfigure((0, 1), weight=1, uniform="check")

        items = [
            ("● Camera Device", "READY", theme.COLOR_SUCCESS),
            ("● Lighting Contrast", "OPTIMAL", theme.COLOR_SUCCESS),
            ("● Stance Distance", "6 - 8 FT RECOMMENDED", theme.COLOR_ACCENT),
            ("● YOLOv8 Pose Engine", "STANDBY", theme.COLOR_ACCENT)
        ]

        for i, (label, val, color) in enumerate(items):
            row = i // 2
            col = i % 2
            card = ctk.CTkFrame(
                self.checklist_frame,
                corner_radius=8,
                fg_color=theme.COLOR_CARD_BG,
                border_width=1,
                border_color=theme.COLOR_BORDER
            )
            card.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

            lbl = ctk.CTkLabel(
                card,
                text=label,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=theme.COLOR_TEXT_PRIMARY
            )
            lbl.pack(anchor="w", padx=10, pady=(6, 1))

            status_lbl = ctk.CTkLabel(
                card,
                text=val,
                font=ctk.CTkFont(size=10),
                text_color=color
            )
            status_lbl.pack(anchor="w", padx=10, pady=(0, 6))

        # ----------------------------------------------------------------------
        # Onboarding Step Guidelines
        # ----------------------------------------------------------------------
        self.steps_frame = ctk.CTkFrame(
            self,
            corner_radius=8,
            fg_color=theme.COLOR_PANEL_BG,
            border_width=1,
            border_color=theme.COLOR_BORDER
        )
        self.steps_frame.pack(fill="x", padx=20, pady=8)

        steps = [
            ("1. Position Camera", "Set lens approximately waist-high with unobstructed floor-to-head visibility."),
            ("2. Clear Workspace", "Ensure 6 to 8 feet of clear space to perform full movement range safely."),
            ("3. Verify Lighting", "Ensure consistent front lighting; avoid strong backlights or dark shadows."),
            ("4. Real-Time Tracking", "YOLO neural network automatically detects joints and begins bio-feedback.")
        ]

        for title, desc in steps:
            row_f = ctk.CTkFrame(self.steps_frame, fg_color="transparent")
            row_f.pack(fill="x", padx=12, pady=3)

            t_lbl = ctk.CTkLabel(
                row_f,
                text=title,
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color=theme.COLOR_ACCENT,
                width=120,
                anchor="w"
            )
            t_lbl.pack(side="left")

            d_lbl = ctk.CTkLabel(
                row_f,
                text=desc,
                font=ctk.CTkFont(size=10),
                text_color=theme.COLOR_TEXT_SECONDARY,
                anchor="w"
            )
            d_lbl.pack(side="left", fill="x", expand=True)

        # ----------------------------------------------------------------------
        # Action Buttons
        # ----------------------------------------------------------------------
        self.actions_row = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_row.pack(fill="x", padx=20, pady=(8, 16))

        if self.on_start:
            self.btn_start = ctk.CTkButton(
                self.actions_row,
                text="START LIVE AI WORKOUT",
                font=ctk.CTkFont(size=theme.FONT_BADGE[1], weight=theme.FONT_BADGE[2]),
                height=36,
                corner_radius=8,
                fg_color=theme.COLOR_PRIMARY,
                hover_color=theme.COLOR_BORDER_LIGHT,
                text_color=theme.COLOR_TEXT_PRIMARY,
                command=self.on_start
            )
            self.btn_start.pack(side="right")
