"""Script to generate cyber-slate reference illustrations for Phase 4 guided exercises:
Push-Up, Lunge, Plank, and Shoulder Press.
"""

import os
from PIL import Image, ImageDraw, ImageFont

BG_COLOR = (13, 19, 31)          # #0D131F
PANEL_BG = (19, 27, 42)          # #131B2A
BORDER = (30, 43, 62)            # #1E2B3E
CYAN = (0, 229, 255)             # #00E5FF
GREEN = (0, 230, 118)            # #00E676
GREEN_MUTED = (13, 43, 30)
WHITE = (248, 250, 252)
SLATE = (148, 163, 184)
AMBER = (255, 145, 0)

def get_fonts():
    try:
        font_title = ImageFont.truetype("segoeuib.ttf", 15)
        font_tag = ImageFont.truetype("segoeuib.ttf", 11)
        font_label = ImageFont.truetype("segoeui.ttf", 10)
        font_bold = ImageFont.truetype("segoeuib.ttf", 10)
    except Exception:
        font_title = ImageFont.load_default()
        font_tag = font_title
        font_label = font_title
        font_bold = font_title
    return font_title, font_tag, font_label, font_bold

def draw_header_and_grid(img, draw, title, subtitle):
    font_title, font_tag, font_label, font_bold = get_fonts()
    # Subtle cyber grid
    for x in range(20, 380, 25):
        draw.line([(x, 35), (x, 155)], fill=(18, 26, 40), width=1)
    for y in range(40, 155, 25):
        draw.line([(20, y), (380, y)], fill=(18, 26, 40), width=1)

    # Title header
    draw.text((20, 12), title, font=font_title, fill=WHITE)
    draw.text((230, 14), subtitle, font=font_tag, fill=CYAN)

def create_pushup_diagram():
    font_title, font_tag, font_label, font_bold = get_fonts()
    img = Image.new("RGB", (400, 160), BG_COLOR)
    d = ImageDraw.Draw(img)
    draw_header_and_grid(img, d, "PUSH-UP FORM", "90° ELBOW DEPTH")

    # Floor line
    d.line([(25, 140), (240, 140)], fill=BORDER, width=2)

    # Human figure in bottom of push-up (profile)
    # Hands: (80, 138), Elbow: (95, 108), Shoulder: (120, 115)
    # Hips: (170, 120), Feet: (225, 136)
    d.line([(80, 138), (95, 108)], fill=CYAN, width=3)   # Forearm
    d.line([(95, 108), (120, 115)], fill=CYAN, width=3)  # Upper arm
    d.line([(120, 115), (225, 136)], fill=GREEN, width=4) # Rigid plank line (shoulder to feet)

    # Nodes
    d.circle((80, 138), 4, fill=WHITE)   # Hand
    d.circle((95, 108), 5, fill=AMBER)   # Elbow (90 deg)
    d.circle((120, 115), 5, fill=GREEN)  # Shoulder
    d.circle((170, 120), 4, fill=GREEN)  # Hip
    d.circle((225, 136), 4, fill=WHITE)  # Feet

    # Head
    d.circle((105, 112), 7, outline=WHITE, width=2)

    # 90 deg arc marker
    d.text((90, 88), "90°", font=font_bold, fill=AMBER)

    # Cues card
    d.rounded_rectangle([250, 42, 385, 140], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 50), "TECHNIQUE CUES", font=font_tag, fill=GREEN)
    d.text((260, 70), "• 180° Rigid Plank", font=font_label, fill=WHITE)
    d.text((260, 86), "• 90° Elbow Flexion", font=font_label, fill=WHITE)
    d.text((260, 102), "• Elbows 45° from Ribs", font=font_label, fill=WHITE)
    d.text((260, 118), "• Neutral Neck", font=font_label, fill=WHITE)

    os.makedirs(os.path.join("assets", "exercises"), exist_ok=True)
    img.save(os.path.join("assets", "exercises", "push_up_reference.png"))

def create_lunge_diagram():
    font_title, font_tag, font_label, font_bold = get_fonts()
    img = Image.new("RGB", (400, 160), BG_COLOR)
    d = ImageDraw.Draw(img)
    draw_header_and_grid(img, d, "LUNGE FORM", "90° DUAL KNEE")

    # Floor line
    d.line([(25, 145), (240, 145)], fill=BORDER, width=2)

    # Lunge figure:
    # Front foot: (85, 145), Front Knee: (85, 100), Hip: (130, 95)
    # Rear Knee: (165, 135), Rear Foot: (200, 145)
    # Torso: Hip (130, 95) to Shoulder (130, 55)
    d.line([(85, 145), (85, 100)], fill=CYAN, width=3)   # Front shin (vertical)
    d.line([(85, 100), (130, 95)], fill=CYAN, width=3)   # Front thigh (horizontal)
    d.line([(130, 95), (130, 55)], fill=GREEN, width=4)  # Torso (upright)
    d.line([(130, 95), (165, 135)], fill=AMBER, width=3) # Rear thigh
    d.line([(165, 135), (200, 145)], fill=AMBER, width=3)# Rear shin

    # Nodes
    d.circle((85, 145), 4, fill=WHITE)
    d.circle((85, 100), 5, fill=GREEN) # 90 front knee
    d.circle((130, 95), 4, fill=WHITE)
    d.circle((130, 55), 4, fill=WHITE)
    d.circle((165, 135), 4, fill=AMBER) # Rear knee hovering
    d.circle((200, 145), 4, fill=WHITE)

    # Head
    d.circle((130, 42), 7, outline=WHITE, width=2)

    # Labels
    d.text((70, 85), "90°", font=font_bold, fill=GREEN)

    # Cues card
    d.rounded_rectangle([250, 42, 385, 140], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 50), "TECHNIQUE CUES", font=font_tag, fill=GREEN)
    d.text((260, 70), "• Vertical Front Shin", font=font_label, fill=WHITE)
    d.text((260, 86), "• 90° Front Knee Angle", font=font_label, fill=WHITE)
    d.text((260, 102), "• Upright Neutral Torso", font=font_label, fill=WHITE)
    d.text((260, 118), "• Rear Knee 1\" Off Floor", font=font_label, fill=WHITE)

    img.save(os.path.join("assets", "exercises", "lunge_reference.png"))

def create_plank_diagram():
    font_title, font_tag, font_label, font_bold = get_fonts()
    img = Image.new("RGB", (400, 160), BG_COLOR)
    d = ImageDraw.Draw(img)
    draw_header_and_grid(img, d, "PLANK FORM", "180° NEUTRAL AXIS")

    # Floor line
    d.line([(25, 140), (240, 140)], fill=BORDER, width=2)

    # Forearm on floor: Elbow (80, 140), Hand (105, 140)
    # Shoulder: (80, 112)
    # Hip: (150, 115)
    # Feet: (220, 138)
    d.line([(80, 140), (105, 140)], fill=WHITE, width=3)  # Forearm flat
    d.line([(80, 140), (80, 112)], fill=CYAN, width=3)   # Upper arm vertical
    d.line([(80, 112), (220, 138)], fill=GREEN, width=4) # 180 spine line

    # Nodes
    d.circle((80, 140), 5, fill=CYAN)  # Elbow under shoulder
    d.circle((80, 112), 5, fill=GREEN) # Shoulder
    d.circle((150, 115), 5, fill=GREEN)# Pelvis / Core
    d.circle((220, 138), 4, fill=WHITE)# Feet

    # Head
    d.circle((65, 110), 7, outline=WHITE, width=2)

    # 180 marker
    d.text((140, 92), "180° NEUTRAL", font=font_bold, fill=GREEN)

    # Cues card
    d.rounded_rectangle([250, 42, 385, 140], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 50), "TECHNIQUE CUES", font=font_tag, fill=GREEN)
    d.text((260, 70), "• Elbow Directly Under Joint", font=font_label, fill=WHITE)
    d.text((260, 86), "• Zero Lumbar Sagging", font=font_label, fill=WHITE)
    d.text((260, 102), "• Glutes & Quads Clenched", font=font_label, fill=WHITE)
    d.text((260, 118), "• Continuous Core Tension", font=font_label, fill=WHITE)

    img.save(os.path.join("assets", "exercises", "plank_reference.png"))

def create_shoulder_press_diagram():
    font_title, font_tag, font_label, font_bold = get_fonts()
    img = Image.new("RGB", (400, 160), BG_COLOR)
    d = ImageDraw.Draw(img)
    draw_header_and_grid(img, d, "SHOULDER PRESS", "170° OVERHEAD")

    # Floor line
    d.line([(25, 148), (240, 148)], fill=BORDER, width=2)

    # Standing figure pressing overhead:
    # Feet (130, 148), Knees (130, 120), Hips (130, 92), Shoulders (130, 62)
    # Left Arm: Shoulder (120, 62) -> Elbow (105, 42) -> Hand (110, 22)
    # Right Arm: Shoulder (140, 62) -> Elbow (155, 42) -> Hand (150, 22)
    # Barbell overhead: (95, 20) to (165, 20)
    d.line([(130, 148), (130, 92)], fill=SLATE, width=3) # Legs
    d.line([(130, 92), (130, 62)], fill=GREEN, width=4)  # Torso (neutral, no arch)

    # Arms pressing up
    d.line([(120, 62), (110, 40)], fill=CYAN, width=3)
    d.line([(110, 40), (115, 22)], fill=CYAN, width=3)
    d.line([(140, 62), (150, 40)], fill=CYAN, width=3)
    d.line([(150, 40), (145, 22)], fill=CYAN, width=3)

    # Bar overhead
    d.line([(100, 20), (160, 20)], fill=AMBER, width=3)

    # Head
    d.circle((130, 50), 7, outline=WHITE, width=2)

    # Nodes
    d.circle((110, 40), 4, fill=CYAN)
    d.circle((150, 40), 4, fill=CYAN)
    d.circle((115, 22), 4, fill=WHITE)
    d.circle((145, 22), 4, fill=WHITE)

    # Cues card
    d.rounded_rectangle([250, 42, 385, 140], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 50), "TECHNIQUE CUES", font=font_tag, fill=GREEN)
    d.text((260, 70), "• Vertical Press Path", font=font_label, fill=WHITE)
    d.text((260, 86), "• Ribs Down (No Back Arch)", font=font_label, fill=WHITE)
    d.text((260, 102), "• Head Pushes Through at Top", font=font_label, fill=WHITE)
    d.text((260, 118), "• Full Elbow Extension", font=font_label, fill=WHITE)

    img.save(os.path.join("assets", "exercises", "shoulder_press_reference.png"))

if __name__ == "__main__":
    create_pushup_diagram()
    create_lunge_diagram()
    create_plank_diagram()
    create_shoulder_press_diagram()
    print("Phase 4 reference diagrams created successfully.")
