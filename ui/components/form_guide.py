"""Correct Posture Reference & Exercise Guidance Component.

Displays visual reference illustrations, biomechanical standards, common mistakes to avoid,
actionable improvement tips, and real-time AI feedback emphasis.
"""

from typing import Optional, Dict, Any, List, Tuple, Callable
import os
from PIL import Image, ImageDraw
import customtkinter as ctk

from ui import theme
from core.exercise_guidance import (
    get_exercise_guidance,
    get_all_supported_exercises,
    get_roadmap_exercises,
    find_guidance_highlight,
    classify_posture_feedback
)
from .body_focus import BodyFocusCard
from .smart_coach import SmartCoachCard
from .form_comparison import FormComparisonCard
from .personalized_plan import PersonalizedPlanCard
from .movement_phase import MovementPhaseCard
from .movement_intelligence import MovementIntelligenceCard



class FormGuideFrame(ctk.CTkFrame):
    """Panel displaying exercise posture references, technique standards, and coaching tips."""

    def __init__(self, master, current_exercise: str = "SQUAT", on_close: Optional[callable] = None, **kwargs):
        super().__init__(
            master,
            corner_radius=16,
            fg_color=theme.COLOR_PANEL_BG,
            border_width=1,
            border_color=theme.COLOR_BORDER,
            **kwargs
        )
        self.current_exercise = current_exercise
        self.on_close = on_close
        self._highlighted_card: Optional[ctk.CTkFrame] = None
        self._highlight_items: List[ctk.CTkFrame] = []

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ======================================================================
        # 1. HEADER SECTION
        # ======================================================================
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=16, pady=(14, 8), sticky="ew")
        self.header_frame.grid_columnconfigure(0, weight=1)

        self.title_group = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.title_group.grid(row=0, column=0, sticky="w")

        self.header_title = ctk.CTkLabel(
            self.title_group,
            text="POSTURE REFERENCE",
            font=ctk.CTkFont(size=theme.FONT_SECTION_HEADER[1], weight=theme.FONT_SECTION_HEADER[2]),
            text_color=theme.COLOR_TEXT_PRIMARY
        )
        self.header_title.pack(side="left", padx=(0, 8))

        self.exercise_badge = ctk.CTkLabel(
            self.title_group,
            text=current_exercise.upper(),
            font=ctk.CTkFont(size=theme.FONT_BADGE[1], weight=theme.FONT_BADGE[2]),
            fg_color=theme.COLOR_ACCENT_MUTED,
            text_color=theme.COLOR_ACCENT,
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.exercise_badge.pack(side="left")

        # Optional close button
        if self.on_close:
            self.btn_close = ctk.CTkButton(
                self.header_frame,
                text="✕",
                width=26,
                height=26,
                corner_radius=6,
                fg_color=theme.COLOR_CARD_BG,
                hover_color=theme.COLOR_BORDER_LIGHT,
                text_color=theme.COLOR_TEXT_SECONDARY,
                command=self.on_close
            )
            self.btn_close.grid(row=0, column=1, sticky="e")

        # Header Divider
        self.header_divider = ctk.CTkFrame(self, height=1, fg_color=theme.COLOR_DIVIDER)
        self.header_divider.grid(row=0, column=0, sticky="sew", padx=16)

        # ======================================================================
        # 2. SCROLLABLE CONTENT BODY
        # ======================================================================
        self.scroll_body = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            corner_radius=0,
            scrollbar_button_color=theme.COLOR_BORDER,
            scrollbar_button_hover_color=theme.COLOR_BORDER_LIGHT
        )
        self.scroll_body.grid(row=1, column=0, padx=12, pady=(4, 12), sticky="nsew")
        self.scroll_body.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------------------------
        # A. Visual Posture Reference Image Card
        # ----------------------------------------------------------------------
        self.img_card = ctk.CTkFrame(
            self.scroll_body,
            corner_radius=10,
            fg_color=theme.COLOR_CARD_INNER,
            border_width=1,
            border_color=theme.COLOR_BORDER
        )
        self.img_card.pack(fill="x", pady=(4, 10))

        self.img_label = ctk.CTkLabel(self.img_card, text="", justify="center")
        self.img_label.pack(padx=8, pady=(8, 4), fill="both", expand=True)

        self.img_caption = ctk.CTkLabel(
            self.img_card,
            text="",
            font=ctk.CTkFont(size=9),
            text_color=theme.COLOR_TEXT_MUTED
        )
        self.img_caption.pack(pady=(0, 6))

        # ----------------------------------------------------------------------
        # B. Biomechanical Target Specs & Muscles
        # ----------------------------------------------------------------------
        self.specs_frame = ctk.CTkFrame(
            self.scroll_body,
            corner_radius=10,
            fg_color=theme.COLOR_CARD_BG,
            border_width=1,
            border_color=theme.COLOR_BORDER
        )
        self.specs_frame.pack(fill="x", pady=6)

        self.specs_title = ctk.CTkLabel(
            self.specs_frame,
            text="BIOMECHANICAL TARGETS",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_ACCENT
        )
        self.specs_title.pack(anchor="w", padx=12, pady=(8, 2))

        self.specs_joint = ctk.CTkLabel(
            self.specs_frame,
            text="",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=theme.COLOR_TEXT_PRIMARY
        )
        self.specs_joint.pack(anchor="w", padx=12, pady=1)

        self.specs_muscles = ctk.CTkLabel(
            self.specs_frame,
            text="",
            font=ctk.CTkFont(size=10),
            text_color=theme.COLOR_TEXT_SECONDARY,
            wraplength=280,
            justify="left"
        )
        self.specs_muscles.pack(anchor="w", padx=12, pady=(1, 8))

        # ----------------------------------------------------------------------
        # C. Biomechanical Body Focus Indicator (Phase 3)
        # ----------------------------------------------------------------------
        self.body_focus_card = BodyFocusCard(self.scroll_body)
        self.body_focus_card.pack(fill="x", pady=6)

        # ----------------------------------------------------------------------
        # D. Smart AI Coach Panel (Phase 3)
        # ----------------------------------------------------------------------
        self.smart_coach_card = SmartCoachCard(self.scroll_body)
        self.smart_coach_card.pack(fill="x", pady=6)

        # ----------------------------------------------------------------------
        # D1. AI Movement Phase Visualization (Phase 6)
        # ----------------------------------------------------------------------
        self.movement_phase_card = MovementPhaseCard(self.scroll_body, current_exercise=current_exercise)
        self.movement_phase_card.pack(fill="x", pady=6)

        # ----------------------------------------------------------------------
        # D1B. AI Movement Intelligence Dashboard (Phase 6)
        # ----------------------------------------------------------------------
        self.movement_intelligence_card = MovementIntelligenceCard(self.scroll_body, current_exercise=current_exercise)
        self.movement_intelligence_card.pack(fill="x", pady=6)

        # ----------------------------------------------------------------------
        # D2. AI Posture vs Ideal Form Comparison (Phase 5)
        # ----------------------------------------------------------------------
        self.form_comparison = FormComparisonCard(self.scroll_body, current_exercise=current_exercise)
        self.form_comparison.pack(fill="x", pady=6)

        # ----------------------------------------------------------------------
        # D3. Personalized AI Improvement Plan Card (Phase 5)
        # ----------------------------------------------------------------------
        self.personalized_plan = PersonalizedPlanCard(self.scroll_body, current_exercise=current_exercise)
        self.personalized_plan.pack(fill="x", pady=6)

        # ----------------------------------------------------------------------
        # E. Correct Form Principles Checklist
        # ----------------------------------------------------------------------
        self.correct_section = ctk.CTkFrame(self.scroll_body, fg_color="transparent")
        self.correct_section.pack(fill="x", pady=6)

        self.correct_title = ctk.CTkLabel(
            self.correct_section,
            text="CORRECT FORM PRINCIPLES",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_SUCCESS
        )
        self.correct_title.pack(anchor="w", pady=(4, 6))

        self.correct_cards_container = ctk.CTkFrame(self.correct_section, fg_color="transparent")
        self.correct_cards_container.pack(fill="x")

        # ----------------------------------------------------------------------
        # D. Common Mistakes to Avoid
        # ----------------------------------------------------------------------
        self.mistakes_section = ctk.CTkFrame(self.scroll_body, fg_color="transparent")
        self.mistakes_section.pack(fill="x", pady=6)

        self.mistakes_title = ctk.CTkLabel(
            self.mistakes_section,
            text="COMMON MISTAKES TO AVOID",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_ALERT
        )
        self.mistakes_title.pack(anchor="w", pady=(4, 6))

        self.mistakes_cards_container = ctk.CTkFrame(self.mistakes_section, fg_color="transparent")
        self.mistakes_cards_container.pack(fill="x")

        # ----------------------------------------------------------------------
        # E. Actionable Improvement Tips
        # ----------------------------------------------------------------------
        self.tips_section = ctk.CTkFrame(self.scroll_body, fg_color="transparent")
        self.tips_section.pack(fill="x", pady=6)

        self.tips_title = ctk.CTkLabel(
            self.tips_section,
            text="HOW TO IMPROVE YOUR FORM",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_WARN
        )
        self.tips_title.pack(anchor="w", pady=(4, 6))

        self.tips_cards_container = ctk.CTkFrame(self.tips_section, fg_color="transparent")
        self.tips_cards_container.pack(fill="x")

        # ----------------------------------------------------------------------
        # F. Exercise Library Roadmap Teaser
        # ----------------------------------------------------------------------
        self.roadmap_card = ctk.CTkFrame(
            self.scroll_body,
            corner_radius=8,
            fg_color=theme.COLOR_CARD_INNER,
            border_width=1,
            border_color=theme.COLOR_BORDER
        )
        self.roadmap_card.pack(fill="x", pady=(10, 8))

        self.roadmap_title = ctk.CTkLabel(
            self.roadmap_card,
            text="AI EXERCISE LIBRARY ROADMAP",
            font=ctk.CTkFont(size=9, weight="bold"),
            text_color=theme.COLOR_TEXT_MUTED
        )
        self.roadmap_title.pack(anchor="w", padx=10, pady=(6, 2))

        roadmap_items = get_roadmap_exercises()
        roadmap_names = " • ".join([v["display_name"].split()[0] for v in roadmap_items.values()])
        self.roadmap_desc = ctk.CTkLabel(
            self.roadmap_card,
            text=f"Active: Squat, Deadlift, Bicep Curl\nComing Soon: {roadmap_names}",
            font=ctk.CTkFont(size=9),
            text_color=theme.COLOR_TEXT_SECONDARY,
            justify="left"
        )
        self.roadmap_desc.pack(anchor="w", padx=10, pady=(0, 6))

        # Initial Population
        self.set_exercise(current_exercise)

    def set_exercise(self, exercise_name: str):
        """Updates all guidance content, reference diagram, and checklist items."""
        self.current_exercise = exercise_name
        self.exercise_badge.configure(text=exercise_name.upper())

        guidance = get_exercise_guidance(exercise_name)

        # 1. Update Reference Diagram
        self._load_reference_image(guidance.get("reference_image"))

        # 2. Update Biomechanical Target Specs
        joint_text = f"Primary Axis: {guidance.get('primary_joint', 'Joint')} • Target: {guidance.get('target_angle', 'Angle')}"
        self.specs_joint.configure(text=joint_text)

        muscles = ", ".join(guidance.get("target_muscles", []))
        self.specs_muscles.configure(text=f"Muscles Engaged: {muscles}")

        # 3. Update Correct Form Principles
        self._populate_cards(
            self.correct_cards_container,
            guidance.get("correct_form", []),
            icon="✔",
            icon_color=theme.COLOR_SUCCESS,
            border_color=theme.COLOR_BORDER
        )

        # 4. Update Common Mistakes
        self._populate_cards(
            self.mistakes_cards_container,
            guidance.get("common_mistakes", []),
            icon="✖",
            icon_color=theme.COLOR_ALERT,
            border_color=theme.COLOR_BORDER
        )

        # 5. Update Improvement Tips
        self._populate_cards(
            self.tips_cards_container,
            guidance.get("improvement_tips", []),
            icon="•",
            icon_color=theme.COLOR_WARN,
            border_color=theme.COLOR_BORDER
        )

        # 6. Reset Phase 5 and Phase 6 components
        if hasattr(self, "movement_phase_card"):
            self.movement_phase_card.set_exercise(exercise_name)
        if hasattr(self, "movement_intelligence_card"):
            self.movement_intelligence_card.reset()
        if hasattr(self, "body_focus_card") and hasattr(self, "smart_coach_card"):
            self.reset_coaching()

    def _get_fallback_image(self, width: int = 280, height: int = 160) -> ctk.CTkImage:
        """Generates a high-tech placeholder card when reference illustration is absent."""
        fallback_pil = Image.new("RGB", (width, height), (13, 19, 31))
        d = ImageDraw.Draw(fallback_pil)
        d.rounded_rectangle([2, 2, width - 3, height - 3], radius=8, outline=(30, 43, 62), width=1)
        d.text((width // 2, height // 2 - 12), "[ POSTURE ILLUSTRATION ]", fill=(0, 229, 255), anchor="mm")
        d.text((width // 2, height // 2 + 12), "Follow Biomechanical Standards Below", fill=(148, 163, 184), anchor="mm")
        return ctk.CTkImage(light_image=fallback_pil, dark_image=fallback_pil, size=(width, height))

    def _load_reference_image(self, image_path: Optional[str]):
        """Safely loads and scales the local reference illustration with zero-crash fallback."""
        if image_path and os.path.isfile(image_path):
            try:
                pil_img = Image.open(image_path)
                # Proportional resize fitting ~280px width
                w, h = pil_img.size
                target_w = 280
                target_h = max(100, int(h * (target_w / max(w, 1))))
                ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(target_w, target_h))
                self.img_label.configure(image=ctk_img, text="")
                self.img_caption.configure(text=f"Optimal {self.current_exercise.upper()} Biomechanical Posture")
                return
            except Exception:
                pass

        # High-tech fallback image if image missing or corrupt
        fallback_img = self._get_fallback_image()
        self.img_label.configure(
            image=fallback_img,
            text=""
        )
        self.img_caption.configure(text=f"Reference standards for {self.current_exercise.upper()}")

    def _populate_cards(
        self,
        container: ctk.CTkFrame,
        items: List[Tuple[str, str]],
        icon: str,
        icon_color: str,
        border_color: str
    ):
        """Populates an item list with rounded guidance cards."""
        # Clear existing
        for child in container.winfo_children():
            child.destroy()

        if container == self.correct_cards_container:
            self._highlight_items = []

        for title, desc in items:
            card = ctk.CTkFrame(
                container,
                corner_radius=8,
                fg_color=theme.COLOR_CARD_BG,
                border_width=1,
                border_color=border_color
            )
            card.pack(fill="x", pady=3)

            # Icon + Title row
            row = ctk.CTkFrame(card, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=(6, 2))

            icon_lbl = ctk.CTkLabel(
                row,
                text=icon,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=icon_color,
                width=16
            )
            icon_lbl.pack(side="left", padx=(0, 6))

            title_lbl = ctk.CTkLabel(
                row,
                text=title,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=theme.COLOR_TEXT_PRIMARY
            )
            title_lbl.pack(side="left")

            # Description
            desc_lbl = ctk.CTkLabel(
                card,
                text=desc,
                font=ctk.CTkFont(size=10),
                text_color=theme.COLOR_TEXT_SECONDARY,
                wraplength=270,
                justify="left"
            )
            desc_lbl.pack(anchor="w", padx=(32, 10), pady=(0, 6))

            if container == self.correct_cards_container:
                self._highlight_items.append(card)

    def highlight_feedback(self, feedback_msg: str):
        """
        Dynamically emphasizes the relevant correct form principle when real-time AI feedback is received.
        Safe keyword mapping without altering backend AI logic.
        """
        match_idx = find_guidance_highlight(self.current_exercise, feedback_msg)

        # Reset previously highlighted card
        if self._highlighted_card:
            self._highlighted_card.configure(
                border_color=theme.COLOR_BORDER,
                border_width=1
            )
            self._highlighted_card = None

        # Highlight matching card
        if match_idx is not None and 0 <= match_idx < len(self._highlight_items):
            target = self._highlight_items[match_idx]
            target.configure(
                border_color=theme.COLOR_ACCENT,
                border_width=2
            )
            self._highlighted_card = target

    def update_ai_coaching(self, feedback_msg: str, feedback_color: str):
        """Synchronizes Body Focus avatar, Smart AI Coach, and checklist highlight."""
        data = classify_posture_feedback(self.current_exercise, feedback_msg, feedback_color)
        self.body_focus_card.set_focus(data["body_focus"], data["focus_label"], data["category"])
        self.smart_coach_card.update_coach(data)
        self.highlight_feedback(feedback_msg)

    def reset_coaching(self):
        """Resets Body Focus and Smart Coach to baseline."""
        self.body_focus_card.reset()
        self.smart_coach_card.reset()
        self.reset_phase5()
        if self._highlighted_card:
            self._highlighted_card.configure(
                border_color=theme.COLOR_BORDER,
                border_width=1
            )
            self._highlighted_card = None

    def update_form_comparison(self, exercise_name: str, feedback_msg: str, feedback_color: Optional[str] = None):
        """Updates the Live vs Ideal form comparison card."""
        if hasattr(self, "form_comparison"):
            self.form_comparison.update_comparison(exercise_name, feedback_msg, feedback_color)

    def update_personalized_plan(self, exercise_name: str):
        """Refreshes the personalized AI plan card."""
        if hasattr(self, "personalized_plan"):
            self.personalized_plan.refresh(exercise_name)

    def reset_phase5(self):
        """Resets Phase 5 comparison and personalized plan."""
        if hasattr(self, "form_comparison"):
            self.form_comparison.reset()
        if hasattr(self, "personalized_plan"):
            self.personalized_plan.refresh(self.current_exercise)

    def update_movement_phase(self, phase_data: Dict[str, Any]):
        """Updates the real-time movement phase visualization card."""
        if hasattr(self, "movement_phase_card"):
            self.movement_phase_card.update_phase(phase_data)

    def update_movement_intelligence(
        self,
        stability_data: Dict[str, Any],
        fatigue_data: Dict[str, Any],
        risk_data: Dict[str, Any],
        coach_data: Dict[str, Any],
        recovery_data: Dict[str, Any]
    ):
        """Updates the AI motion intelligence dashboard card."""
        if hasattr(self, "movement_intelligence_card"):
            self.movement_intelligence_card.update_intelligence(
                stability_data, fatigue_data, risk_data, coach_data, recovery_data
            )

    def reset_phase6(self):
        """Resets Phase 6 movement phase and intelligence cards."""
        if hasattr(self, "movement_phase_card"):
            self.movement_phase_card.reset()
        if hasattr(self, "movement_intelligence_card"):
            self.movement_intelligence_card.reset()

