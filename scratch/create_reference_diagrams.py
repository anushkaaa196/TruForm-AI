import os
import math
from PIL import Image, ImageDraw, ImageFont

def get_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    font_names = (
        ["segoeuib.ttf", "arialbd.ttf", "segoeui.ttf", "arial.ttf"] if bold
        else ["segoeui.ttf", "arial.ttf"]
    )
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            continue
    return ImageFont.load_default()

def create_reference_images():
    os.makedirs(os.path.join("assets", "exercises"), exist_ok=True)
    WIDTH, HEIGHT = 400, 240
    
    font_badge = get_font(10, bold=True)
    font_title = get_font(12, bold=True)
    font_label = get_font(9, bold=False)
    font_tag = get_font(10, bold=True)

    BG = (13, 19, 31)
    GRID = (20, 29, 46)
    BORDER = (30, 43, 62)
    CYAN = (0, 229, 255)
    CYAN_MUTED = (11, 38, 56)
    GREEN = (0, 230, 118)
    GREEN_MUTED = (13, 43, 30)
    WHITE = (248, 250, 252)
    GRAY = (148, 163, 184)
    BONE = (56, 189, 248)

    # --------------------------------------------------------------------------
    # 1. SQUAT REFERENCE
    # --------------------------------------------------------------------------
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    # Subtle Grid
    for x in range(0, WIDTH, 30):
        d.line([x, 0, x, HEIGHT], fill=GRID, width=1)
    for y in range(0, HEIGHT, 30):
        d.line([0, y, WIDTH, y], fill=GRID, width=1)

    # Outer border
    d.rounded_rectangle([2, 2, WIDTH - 3, HEIGHT - 3], radius=8, outline=BORDER, width=1)

    # Top Tag
    d.rounded_rectangle([14, 12, 200, 32], radius=4, fill=CYAN_MUTED, outline=BORDER)
    d.text((22, 16), "SQUAT • POSTURE STANDARD", font=font_badge, fill=CYAN)

    # Floor line
    d.line([60, 205, 340, 205], fill=(45, 62, 88), width=2)
    d.text((70, 210), "GROUND BASELINE (TRIPOD FOOT)", font=font_label, fill=GRAY)

    # Biomechanical Squat Figure (Profile view)
    # Ankle: (150, 205)
    # Knee: (195, 165)
    # Hip: (130, 165) -> Thigh is horizontal (parallel)
    # Shoulder: (165, 105) -> Torso inclined forward naturally
    # Head: (175, 85)
    ankle = (150, 205)
    knee = (200, 160)
    hip = (130, 160)
    shoulder = (165, 100)
    head = (175, 80)
    elbow = (185, 125)
    wrist = (200, 115)

    # Draw Bones
    d.line([ankle, knee], fill=BONE, width=5)        # Shin / Tibia
    d.line([knee, hip], fill=GREEN, width=6)          # Femur (Parallel)
    d.line([hip, shoulder], fill=BONE, width=5)      # Spine
    d.line([shoulder, elbow], fill=GRAY, width=3)
    d.line([elbow, wrist], fill=GRAY, width=3)

    # Draw Joints
    for pt in [ankle, knee, hip, shoulder, elbow, wrist]:
        d.ellipse([pt[0]-5, pt[1]-5, pt[0]+5, pt[1]+5], fill=CYAN, outline=WHITE, width=1)
    d.ellipse([head[0]-10, head[1]-10, head[0]+10, head[1]+10], fill=BONE, outline=WHITE, width=2)

    # Angle indicators & Cues
    d.arc([knee[0]-25, knee[1]-25, knee[0]+25, knee[1]+25], 110, 200, fill=GREEN, width=2)
    d.text((215, 145), "100° Parallel Depth", font=font_badge, fill=GREEN)

    d.line([shoulder[0]-20, shoulder[1]-10, hip[0]-20, hip[1]+10], fill=CYAN, width=1)
    d.text((75, 115), "Neutral Spine\n(Chest Up)", font=font_label, fill=WHITE)

    # Key takeaway card on right
    d.rounded_rectangle([250, 45, 385, 130], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 52), "TARGET DEPTH", font=font_tag, fill=GREEN)
    d.text((260, 72), "• Thighs Parallel", font=font_label, fill=WHITE)
    d.text((260, 88), "• Knees Over Toes", font=font_label, fill=WHITE)
    d.text((260, 104), "• Heels Grounded", font=font_label, fill=WHITE)

    img.save(os.path.join("assets", "exercises", "squat_reference.png"))

    # --------------------------------------------------------------------------
    # 2. DEADLIFT REFERENCE
    # --------------------------------------------------------------------------
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    for x in range(0, WIDTH, 30):
        d.line([x, 0, x, HEIGHT], fill=GRID, width=1)
    for y in range(0, HEIGHT, 30):
        d.line([0, y, WIDTH, y], fill=GRID, width=1)

    d.rounded_rectangle([2, 2, WIDTH - 3, HEIGHT - 3], radius=8, outline=BORDER, width=1)

    # Top Tag
    d.rounded_rectangle([14, 12, 215, 32], radius=4, fill=CYAN_MUTED, outline=BORDER)
    d.text((22, 16), "DEADLIFT • POSTURE STANDARD", font=font_badge, fill=CYAN)

    d.line([60, 205, 340, 205], fill=(45, 62, 88), width=2)
    d.text((70, 210), "GROUND BASELINE (MIDFOOT BALANCE)", font=font_label, fill=GRAY)

    # Biomechanical Deadlift Figure (Hip Hinge)
    # Ankle: (160, 205)
    # Knee: (175, 170) -> slight knee bend, mostly vertical shins
    # Hip: (130, 140)  -> pushed back high
    # Shoulder: (195, 100) -> torso hinged forward
    # Head: (210, 85)
    # Hands: (195, 175) -> straight down
    ankle = (160, 205)
    knee = (175, 170)
    hip = (125, 140)
    shoulder = (195, 95)
    head = (210, 80)
    hands = (195, 175)

    d.line([ankle, knee], fill=BONE, width=5)
    d.line([knee, hip], fill=BONE, width=5)
    d.line([hip, shoulder], fill=GREEN, width=6)    # Rigid neutral spine
    d.line([shoulder, hands], fill=GRAY, width=4)   # Long arms

    # Barbell load circle
    d.ellipse([hands[0]-8, hands[1]-8, hands[0]+8, hands[1]+8], fill=(255, 145, 0), outline=WHITE, width=2)

    for pt in [ankle, knee, hip, shoulder, hands]:
        d.ellipse([pt[0]-5, pt[1]-5, pt[0]+5, pt[1]+5], fill=CYAN, outline=WHITE, width=1)
    d.ellipse([head[0]-10, head[1]-10, head[0]+10, head[1]+10], fill=BONE, outline=WHITE, width=2)

    # Hip Hinge Indicator
    d.arc([hip[0]-25, hip[1]-25, hip[0]+25, hip[1]+25], 300, 360, fill=GREEN, width=2)
    d.text((70, 135), "110° Hip Hinge\n(Glutes Loaded)", font=font_badge, fill=GREEN)

    d.text((205, 115), "Rigid Flat Spine\n(Zero Rounding)", font=font_label, fill=WHITE)

    # Key takeaway card
    d.rounded_rectangle([250, 45, 385, 130], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 52), "HINGE MECHANICS", font=font_tag, fill=GREEN)
    d.text((260, 72), "• Neutral Lumbar", font=font_label, fill=WHITE)
    d.text((260, 88), "• Vertical Shins", font=font_label, fill=WHITE)
    d.text((260, 104), "• Bar Close to Shins", font=font_label, fill=WHITE)

    img.save(os.path.join("assets", "exercises", "deadlift_reference.png"))

    # --------------------------------------------------------------------------
    # 3. BICEP CURL REFERENCE
    # --------------------------------------------------------------------------
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    for x in range(0, WIDTH, 30):
        d.line([x, 0, x, HEIGHT], fill=GRID, width=1)
    for y in range(0, HEIGHT, 30):
        d.line([0, y, WIDTH, y], fill=GRID, width=1)

    d.rounded_rectangle([2, 2, WIDTH - 3, HEIGHT - 3], radius=8, outline=BORDER, width=1)

    # Top Tag
    d.rounded_rectangle([14, 12, 225, 32], radius=4, fill=CYAN_MUTED, outline=BORDER)
    d.text((22, 16), "BICEP CURL • POSTURE STANDARD", font=font_badge, fill=CYAN)

    d.line([60, 205, 340, 205], fill=(45, 62, 88), width=2)
    d.text((70, 210), "GROUND BASELINE (STABLE BIPEDAL STANCE)", font=font_label, fill=GRAY)

    # Biomechanical Bicep Curl Figure (Upright, arm flexed at 65 deg)
    ankle = (160, 205)
    knee = (160, 165)
    hip = (160, 125)
    shoulder = (160, 75)
    head = (160, 50)
    elbow = (165, 115)       # Pinned elbow
    wrist = (195, 85)        # Curled upward to peak contraction

    d.line([ankle, knee], fill=BONE, width=4)
    d.line([knee, hip], fill=BONE, width=4)
    d.line([hip, shoulder], fill=BONE, width=5)      # Upright torso
    d.line([shoulder, elbow], fill=BONE, width=4)    # Upper arm pinned
    d.line([elbow, wrist], fill=GREEN, width=6)      # Forearm curled

    # Dumbbell load circle
    d.ellipse([wrist[0]-7, wrist[1]-7, wrist[0]+7, wrist[1]+7], fill=(255, 145, 0), outline=WHITE, width=2)

    for pt in [ankle, knee, hip, shoulder, elbow, wrist]:
        d.ellipse([pt[0]-5, pt[1]-5, pt[0]+5, pt[1]+5], fill=CYAN, outline=WHITE, width=1)
    d.ellipse([head[0]-10, head[1]-10, head[0]+10, head[1]+10], fill=BONE, outline=WHITE, width=2)

    # Elbow Angle Arc
    d.arc([elbow[0]-25, elbow[1]-25, elbow[0]+25, elbow[1]+25], 240, 315, fill=GREEN, width=2)
    d.text((200, 110), "65° Peak Flexion", font=font_badge, fill=GREEN)

    d.text((80, 85), "Upright Torso\n(Zero Sway)", font=font_label, fill=WHITE)
    d.text((80, 130), "Pinned Elbows\n(At Sides)", font=font_label, fill=CYAN)

    # Key takeaway card
    d.rounded_rectangle([250, 45, 385, 130], radius=6, fill=GREEN_MUTED, outline=BORDER)
    d.text((260, 52), "ISOLATION CUES", font=font_tag, fill=GREEN)
    d.text((260, 72), "• Pinned Elbows", font=font_label, fill=WHITE)
    d.text((260, 88), "• Full Contraction", font=font_label, fill=WHITE)
    d.text((260, 104), "• 2s Lowering Tempo", font=font_label, fill=WHITE)

    img.save(os.path.join("assets", "exercises", "bicep_curl_reference.png"))
    print("Reference illustrations created successfully.")

if __name__ == "__main__":
    create_reference_images()
