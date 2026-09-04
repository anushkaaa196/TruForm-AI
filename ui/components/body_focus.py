"""Biomechanical Body Focus Indicator Component.

Visualizes human anatomical joints and highlights active postural focus areas
(e.g., Spine, Knees, Hips, Elbows) in real time using vector canvas nodes.
"""

from typing import Optional
import tkinter as tk
import customtkinter as ctk
from ui import theme


class BodyFocusCard(ctk.CTkFrame):
    """Card displaying a stylized anatomical avatar highlighting active joint focus."""

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
            text="BODY FOCUS INDICATOR",
            font=ctk.CTkFont(size=theme.FONT_STAT_TITLE[1], weight=theme.FONT_STAT_TITLE[2]),
            text_color=theme.COLOR_ACCENT
        )
        self.title_lbl.pack(side="left")

        self.status_tag = ctk.CTkLabel(
            self.header_row,
            text="MONITORING",
            font=ctk.CTkFont(size=8, weight="bold"),
            fg_color=theme.COLOR_CARD_INNER,
            text_color=theme.COLOR_TEXT_MUTED,
            corner_radius=4,
            padx=6,
            pady=1
        )
        self.status_tag.pack(side="right")

        # ----------------------------------------------------------------------
        # Vector Skeleton Canvas
        # ----------------------------------------------------------------------
        self.canvas_width = 270
        self.canvas_height = 95
        self.canvas = tk.Canvas(
            self,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=theme.COLOR_CARD_INNER,
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=2)

        # ----------------------------------------------------------------------
        # Focus Label Banner
        # ----------------------------------------------------------------------
        self.focus_label = ctk.CTkLabel(
            self,
            text="FULL BODY — OPTIMAL ALIGNMENT",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color=theme.COLOR_SUCCESS,
            justify="center"
        )
        self.focus_label.pack(pady=(4, 8))

        # Initial Draw
        self.set_focus("FULL_BODY", "FULL BODY — OPTIMAL ALIGNMENT", "CORRECT")

    def set_focus(self, body_focus: str, focus_label: str, category: str = "CORRECT"):
        """
        Redraws skeletal nodes and highlights the active joint/region.
        """
        self.canvas.delete("all")
        focus = (body_focus or "FULL_BODY").upper()

        # Accent color depending on severity
        if category == "CRITICAL":
            highlight_color = theme.COLOR_ALERT
            glow_color = "#2A1818"
            status_text = "ATTENTION"
        elif category == "WARNING":
            highlight_color = theme.COLOR_WARN
            glow_color = "#2A2215"
            status_text = "ADJUSTING"
        else:
            highlight_color = theme.COLOR_SUCCESS
            glow_color = "#152620"
            status_text = "ALIGNED"

        normal_line = theme.COLOR_CARD_ELEVATED
        normal_node = theme.COLOR_BORDER

        # Coordinates for centered stylized figure
        cx = self.canvas_width // 2  # 135
        head_y = 14
        neck_y = 26
        shoulder_y = 28
        spine_mid_y = 44
        hip_y = 56
        knee_y = 74
        ankle_y = 88

        # --- BONES / CONNECTORS ---
        # Neck to Shoulders
        self.canvas.create_line(cx - 24, shoulder_y, cx + 24, shoulder_y, fill=normal_line, width=2)
        # Spine
        spine_color = highlight_color if focus == "SPINE" else normal_line
        spine_width = 3 if focus == "SPINE" else 2
        self.canvas.create_line(cx, neck_y, cx, hip_y, fill=spine_color, width=spine_width)

        # Arms
        elbow_color = highlight_color if focus == "ELBOWS" else normal_line
        elbow_w = 3 if focus == "ELBOWS" else 2
        # Left Arm
        self.canvas.create_line(cx - 24, shoulder_y, cx - 38, shoulder_y + 14, fill=elbow_color, width=elbow_w)
        self.canvas.create_line(cx - 38, shoulder_y + 14, cx - 38, shoulder_y + 28, fill=elbow_color, width=elbow_w)
        # Right Arm
        self.canvas.create_line(cx + 24, shoulder_y, cx + 38, shoulder_y + 14, fill=elbow_color, width=elbow_w)
        self.canvas.create_line(cx + 38, shoulder_y + 14, cx + 38, shoulder_y + 28, fill=elbow_color, width=elbow_w)

        # Pelvis
        hip_color = highlight_color if focus == "HIPS" else normal_line
        hip_w = 3 if focus == "HIPS" else 2
        self.canvas.create_line(cx - 16, hip_y, cx + 16, hip_y, fill=hip_color, width=hip_w)

        # Legs
        knee_color = highlight_color if focus == "KNEES" else normal_line
        knee_w = 3 if focus == "KNEES" else 2
        # Left Leg
        self.canvas.create_line(cx - 14, hip_y, cx - 14, knee_y, fill=knee_color, width=knee_w)
        self.canvas.create_line(cx - 14, knee_y, cx - 14, ankle_y, fill=knee_color, width=knee_w)
        # Right Leg
        self.canvas.create_line(cx + 14, hip_y, cx + 14, knee_y, fill=knee_color, width=knee_w)
        self.canvas.create_line(cx + 14, knee_y, cx + 14, ankle_y, fill=knee_color, width=knee_w)

        # --- JOINTS / NODES ---
        def draw_node(x, y, is_active=False, radius=3):
            if is_active:
                # Glow ring
                self.canvas.create_oval(x - radius - 3, y - radius - 3, x + radius + 3, y + radius + 3, outline=highlight_color, width=1)
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=highlight_color, outline=highlight_color)
            else:
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=normal_node, outline=normal_line)

        # Head
        head_active = (focus == "FULL_BODY")
        head_color = highlight_color if head_active else normal_node
        self.canvas.create_oval(cx - 7, head_y - 7, cx + 7, head_y + 7, outline=head_color, width=2)

        # Shoulders
        draw_node(cx - 24, shoulder_y, focus == "FULL_BODY")
        draw_node(cx + 24, shoulder_y, focus == "FULL_BODY")

        # Elbows
        draw_node(cx - 38, shoulder_y + 14, focus in ("ELBOWS", "FULL_BODY"))
        draw_node(cx + 38, shoulder_y + 14, focus in ("ELBOWS", "FULL_BODY"))

        # Spine (Lumbar Node)
        draw_node(cx, spine_mid_y, focus in ("SPINE", "FULL_BODY"), radius=4 if focus == "SPINE" else 3)

        # Hips
        draw_node(cx - 14, hip_y, focus in ("HIPS", "FULL_BODY"))
        draw_node(cx + 14, hip_y, focus in ("HIPS", "FULL_BODY"))

        # Knees
        draw_node(cx - 14, knee_y, focus in ("KNEES", "FULL_BODY"), radius=4 if focus == "KNEES" else 3)
        draw_node(cx + 14, knee_y, focus in ("KNEES", "FULL_BODY"), radius=4 if focus == "KNEES" else 3)

        # Ankles / Feet
        draw_node(cx - 14, ankle_y, focus == "FULL_BODY")
        draw_node(cx + 14, ankle_y, focus == "FULL_BODY")

        # Update Banner text & colors
        self.focus_label.configure(text=focus_label, text_color=highlight_color)
        self.status_tag.configure(text=status_text, text_color=highlight_color)

    def reset(self):
        """Resets to baseline full-body optimal state."""
        self.set_focus("FULL_BODY", "FULL BODY — OPTIMAL ALIGNMENT", "CORRECT")
