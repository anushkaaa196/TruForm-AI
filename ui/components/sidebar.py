"""Sidebar component containing controls, telemetry stats, and exercise options."""

from typing import Callable, Optional, List
import customtkinter as ctk
from ui import theme


class SidebarFrame(ctk.CTkFrame):
    """Sidebar widget with branding, exercise selection, telemetry card, and actions."""

    def __init__(
        self,
        master,
        exercise_list: List[str],
        on_exercise_selected: Optional[Callable[[str], None]] = None,
        on_toggle_session: Optional[Callable[[], None]] = None,
        on_export_report: Optional[Callable[[], None]] = None,
        on_reset_metrics: Optional[Callable[[], None]] = None,
        **kwargs
    ):
        super().__init__(master, width=280, corner_radius=15, **kwargs)
        self.grid_propagate(False)

        self.on_exercise_selected = on_exercise_selected
        self.on_toggle_session = on_toggle_session
        self.on_export_report = on_export_report
        self.on_reset_metrics = on_reset_metrics

        # Branding
        self.logo_label = ctk.CTkLabel(
            self,
            text="FIT.AI PRO",
            font=ctk.CTkFont(size=theme.FONT_BRAND[1], weight=theme.FONT_BRAND[2])
        )
        self.logo_label.pack(padx=20, pady=(20, 5))

        self.subtitle = ctk.CTkLabel(
            self,
            text="Precision Pose Engine",
            font=ctk.CTkFont(size=theme.FONT_SUBTITLE[1]),
            text_color="gray"
        )
        self.subtitle.pack(padx=20, pady=(0, 15))

        # Exercise Menu Selection
        self.sel_label = ctk.CTkLabel(
            self,
            text="EXERCISE SELECTION",
            font=ctk.CTkFont(size=theme.FONT_SECTION_HEADER[1], weight=theme.FONT_SECTION_HEADER[2])
        )
        self.sel_label.pack(padx=20, pady=(10, 5), anchor="w")

        self.exercise_opt = ctk.CTkOptionMenu(
            self,
            values=exercise_list,
            command=self._handle_exercise_change,
            height=35,
            font=ctk.CTkFont(size=theme.FONT_OPTION_MENU[1], weight=theme.FONT_OPTION_MENU[2])
        )
        self.exercise_opt.pack(padx=20, pady=5, fill="x")

        # Telemetry Metrics Card
        self.stats_card = ctk.CTkFrame(self, corner_radius=10, fg_color=theme.COLOR_CARD_BG)
        self.stats_card.pack(padx=15, pady=15, fill="x")

        self.rep_title = ctk.CTkLabel(
            self.stats_card,
            text="CLEAN REPS",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1]),
            text_color=theme.COLOR_MUTED
        )
        self.rep_title.pack(pady=(10, 0))

        self.rep_val = ctk.CTkLabel(
            self.stats_card,
            text="0",
            font=ctk.CTkFont(size=theme.FONT_STAT_LARGE[1], weight=theme.FONT_STAT_LARGE[2]),
            text_color=theme.COLOR_ACCENT
        )
        self.rep_val.pack(pady=(0, 5))

        self.acc_title = ctk.CTkLabel(
            self.stats_card,
            text="FORM QUALITY ACCURACY",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1]),
            text_color=theme.COLOR_MUTED
        )
        self.acc_title.pack(pady=(5, 0))

        self.acc_val = ctk.CTkLabel(
            self.stats_card,
            text="100%",
            font=ctk.CTkFont(size=theme.FONT_STAT_MEDIUM[1], weight=theme.FONT_STAT_MEDIUM[2]),
            text_color=theme.COLOR_ACCENT
        )
        self.acc_val.pack(pady=(0, 10))

        # Action Buttons
        self.btn_toggle = ctk.CTkButton(
            self,
            text="START WORKOUT",
            fg_color=theme.COLOR_PRIMARY,
            hover_color=theme.COLOR_PRIMARY_HOVER,
            height=40,
            font=ctk.CTkFont(size=theme.FONT_BUTTON_LARGE[1], weight=theme.FONT_BUTTON_LARGE[2]),
            command=self._handle_toggle
        )
        self.btn_toggle.pack(padx=20, pady=(10, 5), fill="x")

        self.btn_report = ctk.CTkButton(
            self,
            text="EXPORT REPORT",
            fg_color=theme.COLOR_INFO,
            hover_color=theme.COLOR_INFO_HOVER,
            height=35,
            command=self._handle_report
        )
        self.btn_report.pack(padx=20, pady=5, fill="x")

        self.btn_reset = ctk.CTkButton(
            self,
            text="RESET METRICS",
            fg_color=theme.COLOR_DANGER,
            hover_color=theme.COLOR_DANGER_HOVER,
            height=35,
            command=self._handle_reset
        )
        self.btn_reset.pack(padx=20, pady=5, fill="x")

    def _handle_exercise_change(self, choice: str):
        if self.on_exercise_selected:
            self.on_exercise_selected(choice)

    def _handle_toggle(self):
        if self.on_toggle_session:
            self.on_toggle_session()

    def _handle_report(self):
        if self.on_export_report:
            self.on_export_report()

    def _handle_reset(self):
        if self.on_reset_metrics:
            self.on_reset_metrics()

    def set_session_state(self, is_running: bool):
        """Updates start/stop button label and color."""
        if is_running:
            self.btn_toggle.configure(
                text="STOP WORKOUT",
                fg_color=theme.COLOR_DANGER,
                hover_color=theme.COLOR_DANGER_HOVER
            )
        else:
            self.btn_toggle.configure(
                text="START WORKOUT",
                fg_color=theme.COLOR_PRIMARY,
                hover_color=theme.COLOR_PRIMARY_HOVER
            )

    def update_stats(self, reps: int, acc: int):
        """Updates metrics values and dynamic accuracy color."""
        self.rep_val.configure(text=str(reps))
        acc_color = (
            theme.COLOR_ACCENT if acc >= 80
            else theme.COLOR_WARN if acc >= 50
            else theme.COLOR_ALERT
        )
        self.acc_val.configure(text=f"{acc}%", text_color=acc_color)
