"""Centralized exercise guidance, biomechanical reference standards, and posture data architecture.

Provides structured educational content, correct form principles, common mistakes,
improvement tips, and scalable definitions for current and future exercises.
"""

from typing import Dict, Any, List, Tuple, Optional
import os


# ==============================================================================
# 1. ACTIVE SUPPORTED EXERCISES
# ==============================================================================
SUPPORTED_EXERCISES: Dict[str, Dict[str, Any]] = {
    "SQUAT": {
        "id": "SQUAT",
        "display_name": "Bodyweight / Barbell Squat",
        "category": "Lower Body Compound",
        "primary_joint": "Knee & Hip",
        "target_angle": "100° (Parallel Depth)",
        "target_muscles": ["Quadriceps", "Glutes", "Hamstrings", "Core Stabilizers"],
        "difficulty": "Beginner to Intermediate",
        "reference_image": os.path.join("assets", "exercises", "squat_reference.png"),
        "key_metrics": {
            "depth_target": "100° knee flexion",
            "torso_minimum": "35° forward inclination max",
            "lockout_angle": "148° standing extension"
        },
        "correct_form": [
            ("Neutral Spine", "Keep your chest lifted, shoulders back, and maintain natural lumbar curvature."),
            ("Knee Alignment", "Track knees in line with toes throughout; prevent any inward knee collapse."),
            ("Tripod Foot Base", "Distribute bodyweight evenly across heel, big toe base, and outer foot edge."),
            ("Parallel Depth", "Descend with control until the hip crease reaches parallel with top of knees."),
            ("Ascent Drive", "Drive upward through midfoot, extending hips and knees in unison to full lockout.")
        ],
        "common_mistakes": [
            ("Knee Valgus (Inward Collapse)", "Knees caving inward during movement strains ACL and medial ligaments."),
            ("Excessive Torso Lean", "Forward chest collapse transfers load from legs to lower back."),
            ("Heels Rising", "Lifting heels off the ground indicates ankle mobility restriction or poor balance."),
            ("Incomplete Depth", "Stopping well above parallel diminishes glute and hamstring muscle activation."),
            ("Passive Chair Sitting", "Resting bodyweight completely on a chair or bench relaxes stabilizer muscles.")
        ],
        "improvement_tips": [
            ("Cadence & Tempo", "Perform a 2-second controlled eccentric descent followed by a 1-second upward drive."),
            ("Foot Stance", "Set feet shoulder-width apart with toes flared naturally outward at 15° to 30°."),
            ("Core Bracing", "Take a diaphragmatic breath and brace abdominal wall before initiating each descent."),
            ("Visual Target", "Focus eyes on a fixed spot at eye level to prevent neck strain and chest collapse.")
        ],
        "keyword_map": {
            "knee": 1,        # Maps to Knee Alignment
            "valgus": 1,
            "chest": 0,       # Maps to Neutral Spine
            "torso": 0,
            "lean": 0,
            "back": 0,
            "foot": 2,        # Maps to Tripod Foot Base
            "heel": 2,
            "depth": 3,       # Maps to Parallel Depth
            "shallow": 3,
            "sitting": 4      # Maps to Ascent Drive / Passive Sitting
        }
    },

    "DEADLIFT": {
        "id": "DEADLIFT",
        "display_name": "Conventional Hip-Hinge Deadlift",
        "category": "Posterior Chain Compound",
        "primary_joint": "Hip & Lumbar Spine",
        "target_angle": "110° (Hip Hinge Apex)",
        "target_muscles": ["Hamstrings", "Gluteus Maximus", "Erector Spinae", "Latissimus Dorsi"],
        "difficulty": "Intermediate",
        "reference_image": os.path.join("assets", "exercises", "deadlift_reference.png"),
        "key_metrics": {
            "hinge_target": "110° hip angle",
            "torso_minimum": "30° minimum inclination",
            "lockout_angle": "150° full hip extension"
        },
        "correct_form": [
            ("Rigid Neutral Spine", "Lock spine straight from cervical neck to coccyx; avoid lumbar rounding."),
            ("Hip Hinge Drive", "Push hips backward as torso hinges forward, loading hamstrings and glutes."),
            ("Close Center of Mass", "Keep resistance or arms close to shins and thighs throughout the vertical path."),
            ("Foot Grounding", "Plant feet hip-width apart; drive through the floor as if pushing the earth away."),
            ("Complete Lockout", "Stand tall with glutes clenched at top without hyperextending lower back.")
        ],
        "common_mistakes": [
            ("Spinal Rounding (Cat Back)", "Rounding the lower or upper back under load places dangerous shear stress on spinal discs."),
            ("Squatting the Lift", "Dropping hips too low converts the hip-hinge into a squat and reduces posterior chain loading."),
            ("Hyperextension at Top", "Leaning backward past vertical at lockout compresses lumbar vertebrae."),
            ("Bar / Hand Drift", "Allowing hands to drift forward away from shins increases leverage against lower back."),
            ("Jerking the Motion", "Yanking upward abruptly rather than building smooth wedge tension.")
        ],
        "improvement_tips": [
            ("Lat Engagement", "Imagine squeezing oranges in your armpits to pack lats and stabilize upper torso."),
            ("Shin Angle", "Keep shins nearly vertical during the hinge to maximize hamstring stretch."),
            ("Slack Removal", "Build tension against the ground before pulling to ensure stable movement initiation."),
            ("Controlled Lowering", "Reverse the movement by hinging hips back first before bending knees on descent.")
        ],
        "keyword_map": {
            "spine": 0,       # Maps to Rigid Neutral Spine
            "back": 0,
            "lean": 0,
            "torso": 0,
            "hip": 1,         # Maps to Hip Hinge Drive
            "hinge": 1,
            "bar": 2,         # Maps to Close Center of Mass
            "arm": 2,
            "foot": 3,        # Maps to Foot Grounding
            "lockout": 4      # Maps to Complete Lockout
        }
    },

    "BICEP_CURL": {
        "id": "BICEP_CURL",
        "display_name": "Standing Dual-Arm Bicep Curl",
        "category": "Upper Body Isolation",
        "primary_joint": "Elbow Joint",
        "target_angle": "65° (Peak Flexion Contraction)",
        "target_muscles": ["Biceps Brachii", "Brachialis", "Brachioradialis", "Forearm Flexors"],
        "difficulty": "Beginner",
        "reference_image": os.path.join("assets", "exercises", "bicep_curl_reference.png"),
        "key_metrics": {
            "flexion_apex": "65° elbow angle",
            "extension_lockout": "125° elbow angle",
            "ascent_threshold": "85° lowering hysteresis"
        },
        "correct_form": [
            ("Pinned Elbows", "Anchor elbows firmly against ribcage; prevent elbows from drifting forward or backward."),
            ("Strict Torso Posture", "Stand tall with chest proud and core braced; eliminate any backward torso sway."),
            ("Full Contraction Peak", "Curl forearm upward until biceps are fully contracted at approximately 60-65°."),
            ("Controlled Eccentric", "Lower with steady resistance over 2 seconds to full arm extension lockout."),
            ("Bilateral Symmetry", "Ensure left and right arms move synchronously without asymmetrical favoring.")
        ],
        "common_mistakes": [
            ("Torso Momentum & Heaving", "Swinging the upper body backward steals tension from the biceps and stresses lumbar spine."),
            ("Elbow Flare / Drift", "Allowing elbows to swing forward converts the curl into a front deltoid raise."),
            ("Incomplete Range of Motion", "Failing to fully extend at bottom limits muscle stretch and growth stimulus."),
            ("Wrist Hyperextension", "Letting wrists bend backward under load strains wrist flexor tendons."),
            ("Rushed Descent", "Dropping arms rapidly without controlling the eccentric phase loses 50% of the training benefit.")
        ],
        "improvement_tips": [
            ("Elbow Pivot Cue", "Visualize your elbows glued to a table so only the forearm rotates on an axis."),
            ("Tempo Discipline", "Curl upward dynamically in 1 second, squeeze for 1 second, and lower in 2 seconds."),
            ("Grip Tension", "Grip firmly with pinky and ring fingers to enhance bicep peak contraction."),
            ("Core Stabilization", "Squeeze glutes and abdominal muscles to create an immovable upper-body pillar.")
        ],
        "keyword_map": {
            "elbow": 0,       # Maps to Pinned Elbows
            "drift": 0,
            "torso": 1,       # Maps to Strict Torso Posture
            "swing": 1,
            "momentum": 1,
            "peak": 2,        # Maps to Full Contraction Peak
            "curl": 2,
            "depth": 3,       # Maps to Controlled Eccentric
            "lockout": 3,
            "arm": 4          # Maps to Bilateral Symmetry
        }
    }
}


# ==============================================================================
# 2. GUIDED / LEARNING MODE EXERCISE GUIDANCE (Full Posture Reference & Cues)
# ==============================================================================
GUIDED_EXERCISES_GUIDANCE: Dict[str, Dict[str, Any]] = {
    "PUSH_UP": {
        "id": "PUSH_UP",
        "display_name": "Standard Floor Push-Up",
        "category": "Upper Body Horizontal Push",
        "primary_joint": "Elbow & Shoulder",
        "target_angle": "90° (Elbow Depth)",
        "target_muscles": ["Pectoralis Major", "Triceps Brachii", "Anterior Deltoids", "Core Stabilizers"],
        "difficulty": "Beginner to Intermediate",
        "reference_image": os.path.join("assets", "exercises", "push_up_reference.png"),
        "key_metrics": {
            "depth_target": "90° elbow flexion",
            "body_alignment": "180° rigid plank axis",
            "lockout_angle": "175° elbow extension"
        },
        "correct_form": [
            ("Rigid Plank Line", "Maintain an unbroken straight line from crown to heels; engage glutes and quads."),
            ("90° Elbow Flexion", "Lower until chest is 2-3 inches above the floor and elbows form a 90° angle."),
            ("45° Arm Angle", "Tuck elbows at approximately 45° relative to your torso, avoiding a flared 'T' shape."),
            ("Neutral Neck Alignment", "Keep gaze about 6 inches ahead of fingers to prevent cervical neck hyperextension."),
            ("Full Lockout Drive", "Push the floor away through palms to reach complete arm extension without shrugging.")
        ],
        "common_mistakes": [
            ("Lumbar Sagging", "Allowing hips to drop transfers harmful hyperextension stress to the lower back."),
            ("Flared Elbows (T-Shape)", "Flaring elbows straight out to 90° puts heavy impingement strain on rotator cuffs."),
            ("Half Reps", "Stopping well before 90° elbow depth significantly reduces chest muscle hypertrophy."),
            ("Leading with Chin", "Reaching neck towards floor gives a false perception of achieving full depth."),
            ("Piked Hips", "Shooting hips up into an inverted-V shifts loading away from the pectoral muscles.")
        ],
        "improvement_tips": [
            ("Incline Progression", "If floor push-ups cause form breakdown, elevate hands on a stable box or bench."),
            ("Cadence Control", "Use a 2-second controlled descent, brief pause, and explosive 1-second push."),
            ("Hand Torque", "Screw palms into the floor to activate lats and lock shoulder capsules in place."),
            ("Abdominal Hollow", "Pull belly button toward spine to lock the pelvis in a neutral position.")
        ],
        "keyword_map": {
            "plank": 0,
            "spine": 0,
            "sag": 0,
            "elbow": 1,
            "depth": 1,
            "flare": 2,
            "neck": 3,
            "lockout": 4
        }
    },

    "LUNGE": {
        "id": "LUNGE",
        "display_name": "Walking / Forward Lunge",
        "category": "Unilateral Lower Body",
        "primary_joint": "Front Knee & Rear Knee",
        "target_angle": "90° Front / 90° Rear Knee",
        "target_muscles": ["Quadriceps", "Gluteus Medius", "Hamstrings", "Calves"],
        "difficulty": "Intermediate",
        "reference_image": os.path.join("assets", "exercises", "lunge_reference.png"),
        "key_metrics": {
            "front_knee_target": "90° flexion, vertical shin",
            "rear_knee_target": "90° flexion, hovering 1 inch off floor",
            "torso_angle": "Vertical 90° spine angle"
        },
        "correct_form": [
            ("Vertical Front Shin", "Keep front shin perpendicular to the floor with knee directly above ankle."),
            ("Dual 90° Angles", "Lower until both front and rear knees achieve approximately 90° flexion."),
            ("Upright Torso", "Maintain vertical posture with shoulders directly stacked above the hips."),
            ("Tripod Foot Base", "Ground the front foot firmly through heel and ball without lifting toes."),
            ("Controlled Descent", "Hover rear knee 1 inch off the floor without slamming kneecap into ground.")
        ],
        "common_mistakes": [
            ("Forward Knee Drift", "Front knee pushing excessively past toes overloads the patellar tendon."),
            ("Torso Leaning Forward", "Collapsing chest over front thigh reduces glute activation and strains back."),
            ("Narrow Stance (Tightrope)", "Placing feet in a straight line degrades balance and lateral hip control."),
            ("Rear Knee Impact", "Dropping down abruptly to bang the back knee onto hard flooring."),
            ("Front Heel Lifting", "Shifting weight onto front toes indicates poor ankle mobility or short stance.")
        ],
        "improvement_tips": [
            ("Railroad Track Stance", "Keep feet hip-width apart throughout the step to maximize balance."),
            ("Glute Squeeze", "Clench rear glute at the bottom to stabilize pelvis and open hip flexor."),
            ("Midfoot Drive", "Push through front midfoot and heel to return smoothly to starting stance."),
            ("Visual Anchor", "Fix eyes at eye level to prevent equilibrium loss during stepping.")
        ],
        "keyword_map": {
            "knee": 0,
            "shin": 0,
            "depth": 1,
            "torso": 2,
            "lean": 2,
            "foot": 3,
            "heel": 3,
            "rear": 4
        }
    },

    "PLANK": {
        "id": "PLANK",
        "display_name": "Isometric Forearm Plank",
        "category": "Core Stability & Anti-Extension",
        "primary_joint": "Spine & Pelvis (Isometric)",
        "target_angle": "180° Neutral Line",
        "target_muscles": ["Rectus Abdominis", "Transverse Abdominis", "Glutes", "Shoulder Girdle"],
        "difficulty": "Beginner",
        "reference_image": os.path.join("assets", "exercises", "plank_reference.png"),
        "key_metrics": {
            "spine_axis": "180° straight line crown to heels",
            "elbow_stack": "Elbows directly under shoulder sockets",
            "hold_duration": "30-60s active isometric tension"
        },
        "correct_form": [
            ("Stacked Elbows", "Position elbows directly beneath shoulders to eliminate shoulder shear stress."),
            ("180° Rigid Axis", "Maintain continuous horizontal alignment from ears through shoulders, hips, and ankles."),
            ("Posterior Pelvic Tilt", "Tuck tailbone slightly under to maximally engage the transverse abdominis."),
            ("Active Shoulder Push", "Press forearms into floor to prevent shoulder blades from winging together."),
            ("Rhythmic Breathing", "Maintain steady diaphragmatic breaths without holding air in lungs.")
        ],
        "common_mistakes": [
            ("Anterior Pelvic Sag", "Allowing belly and hips to drop creates dangerous lumbar compression."),
            ("Piked Hips", "Elevating hips above shoulder level relieves tension from abdominal muscles."),
            ("Hyperextended Neck", "Looking up or craning neck strains the upper cervical vertebrae."),
            ("Collapsed Chest", "Letting chest sink between shoulders pinches upper back joints."),
            ("Holding Breath", "Valsalva breath-holding increases blood pressure without added stability.")
        ],
        "improvement_tips": [
            ("Quality Over Duration", "Prioritize a rock-solid 30-second hold over an unsteady 2-minute sag."),
            ("Isometric Tension", "Actively pull elbows toward toes to create intense full-body bracing."),
            ("Glute Clamp", "Clench glutes with 100% effort to anchor the pelvis and offload lower back."),
            ("Forearm Parallel", "Keep forearms parallel on the floor rather than clasping hands into a triangle.")
        ],
        "keyword_map": {
            "elbow": 0,
            "shoulder": 0,
            "axis": 1,
            "spine": 1,
            "sag": 1,
            "hip": 2,
            "neck": 3,
            "breath": 4
        }
    },

    "SHOULDER_PRESS": {
        "id": "SHOULDER_PRESS",
        "display_name": "Overhead Barbell / DB Press",
        "category": "Upper Body Vertical Push",
        "primary_joint": "Shoulder & Elbow Extension",
        "target_angle": "170° (Overhead Lockout)",
        "target_muscles": ["Anterior & Lateral Deltoids", "Triceps Brachii", "Upper Trapezius", "Core"],
        "difficulty": "Intermediate",
        "reference_image": os.path.join("assets", "exercises", "shoulder_press_reference.png"),
        "key_metrics": {
            "overhead_lockout": "170° elbow extension",
            "press_trajectory": "Vertical bar path clearing head",
            "torso_angle": "Rigid upright torso, zero backward arch"
        },
        "correct_form": [
            ("Vertical Bar Path", "Press directly upward in a straight line passing close in front of the nose."),
            ("Ribcage Down", "Brace abs tightly to keep front ribs down; do not arch back into an incline bench."),
            ("Head Window", "Once the bar clears the forehead, push head slightly through the arms at top."),
            ("Stacked Wrists", "Keep wrists straight directly over elbows; avoid backward wrist bending."),
            ("Full Overhead Lockout", "Extend arms completely at peak with shoulders actively shrugging upward.")
        ],
        "common_mistakes": [
            ("Lumbar Hyperextension", "Leaning backward past vertical compresses lower back and indicates excessive load."),
            ("Bent Wrists", "Allowing bar to roll back into fingers strains wrist tendons and leaks power."),
            ("Flared Elbows at Start", "Tucking elbows behind the body places deltoids in an awkward leverage position."),
            ("Incomplete Lockout", "Stopping short of overhead extension robs triceps and upper traps of full activation."),
            ("Bouncing Knees", "Using leg drive turns an isolated overhead press into a push press.")
        ],
        "improvement_tips": [
            ("Grip Width", "Place hands just outside shoulders so forearms remain strictly vertical from front."),
            ("Glute Lock", "Squeeze glutes tightly throughout the press to establish a stable pelvic foundation."),
            ("Elbows Slightly Forward", "Point elbows slightly inward (30°) at the bottom to protect rotator cuffs."),
            ("Active Traps", "At the top, push upward into the bar as if trying to touch the ceiling.")
        ],
        "keyword_map": {
            "bar": 0,
            "path": 0,
            "rib": 1,
            "lean": 1,
            "back": 1,
            "head": 2,
            "wrist": 3,
            "lockout": 4
        }
    }
}


# ==============================================================================
# 3. ROADMAP / UPCOMING EXERCISES (Scalable Extension Architecture)
# ==============================================================================
ROADMAP_EXERCISES: Dict[str, Dict[str, Any]] = {
    "PUSH_UP": {
        "id": "PUSH_UP",
        "display_name": "Standard Floor Push-Up",
        "category": "Upper Body Horizontal Push",
        "primary_joint": "Elbow & Shoulder",
        "target_angle": "90° (Elbow Depth)",
        "target_muscles": ["Pectoralis Major", "Anterior Deltoids", "Triceps Brachii", "Core"],
        "planned_landmarks": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "planned_criteria": "Maintain 180° straight rigid plank line from shoulders to ankles while bending elbows to 90°.",
        "status": "Guided Mode Active • Backend Analysis In Pipeline"
    },
    "LUNGE": {
        "id": "LUNGE",
        "display_name": "Forward Alternating Lunge",
        "category": "Unilateral Lower Body",
        "primary_joint": "Front Knee & Rear Knee",
        "target_angle": "90° Front / 90° Rear Knee",
        "target_muscles": ["Quadriceps", "Gluteus Medius", "Hamstrings", "Calves"],
        "planned_landmarks": [11, 12, 13, 14, 15, 16],
        "planned_criteria": "Front knee tracks over second toe; rear knee hovers 1 inch above floor with upright torso.",
        "status": "Guided Mode Active • Backend Analysis In Pipeline"
    },
    "PLANK": {
        "id": "PLANK",
        "display_name": "Isometric Forearm Plank",
        "category": "Core Stability & Anti-Extension",
        "primary_joint": "Spine & Pelvis (Isometric Hold)",
        "target_angle": "180° Neutral Body Line",
        "target_muscles": ["Rectus Abdominis", "Transverse Abdominis", "Glutes", "Shoulder Girdle"],
        "planned_landmarks": [5, 6, 11, 12, 13, 14, 15, 16],
        "planned_criteria": "Zero lumbar sagging (anterior pelvic tilt) or hip pike; hold duration timing algorithm.",
        "status": "Guided Mode Active • Backend Analysis In Pipeline"
    },
    "SHOULDER_PRESS": {
        "id": "SHOULDER_PRESS",
        "display_name": "Overhead Overhead Press",
        "category": "Upper Body Vertical Push",
        "primary_joint": "Shoulder & Elbow",
        "target_angle": "170° (Overhead Lockout)",
        "target_muscles": ["Deltoids (Anterior & Lateral)", "Upper Trapezius", "Triceps Brachii"],
        "planned_landmarks": [5, 6, 7, 8, 9, 10, 11, 12],
        "planned_criteria": "Vertical bar path above crown; neutral ribs down without lumbar hyperextension.",
        "status": "Guided Mode Active • Backend Analysis In Pipeline"
    }
}


# ==============================================================================
# 4. PUBLIC ACCESSOR & UTILITY METHODS
# ==============================================================================
def get_exercise_guidance(exercise_name: str) -> Dict[str, Any]:
    """
    Returns the comprehensive guidance dictionary for a given exercise.
    Supports all active and guided exercises with fallback to SQUAT.
    """
    key = exercise_name.upper().strip()
    if key in SUPPORTED_EXERCISES:
        return SUPPORTED_EXERCISES[key]
    if key in GUIDED_EXERCISES_GUIDANCE:
        return GUIDED_EXERCISES_GUIDANCE[key]
    # Default fallback
    return SUPPORTED_EXERCISES["SQUAT"]



def get_all_supported_exercises() -> List[str]:
    """Returns list of currently supported exercise keys."""
    return list(SUPPORTED_EXERCISES.keys())


def get_roadmap_exercises() -> Dict[str, Dict[str, Any]]:
    """Returns metadata dictionary of upcoming exercises in development."""
    return ROADMAP_EXERCISES


def find_guidance_highlight(exercise_name: str, feedback_msg: str) -> Optional[int]:
    """
    Matches keywords from real-time AI feedback to index of corresponding correct form item.
    Enables real-time dynamic visual emphasis in the form guide without modifying backend logic.

    Returns:
        Optional[int]: Index of matched correct_form item, or None if no match.
    """
    guidance = get_exercise_guidance(exercise_name)
    keyword_map = guidance.get("keyword_map", {})
    lower_msg = feedback_msg.lower()

    for kw, index in keyword_map.items():
        if kw in lower_msg:
            return index

    return None


def classify_posture_feedback(
    exercise_name: str,
    feedback_msg: str,
    feedback_color: str
) -> Dict[str, Any]:
    """
    Intelligently categorizes real-time backend feedback into high-value coaching observations,
    concrete actions, priority levels, body focus regions, and next-rep guidance.
    Strictly rule-based and derived from verified backend messages.
    """
    msg_lower = (feedback_msg or "").lower()
    color_upper = (feedback_color or "").upper()
    ex_upper = (exercise_name or "SQUAT").upper()

    # Determine Severity Category & Priority
    if color_upper in ("#00E676", "#00C853") or any(k in msg_lower for k in ["clean", "optimal", "good"]):
        category = "CORRECT"
        priority = "LOW"
        status_label = "OPTIMAL FORM"
    elif color_upper in ("#FF1744", "#D50000") or any(k in msg_lower for k in ["disqualif", "sitting", "error", "fault"]):
        category = "CRITICAL"
        priority = "HIGH"
        status_label = "CRITICAL CORRECTION"
    elif any(k in msg_lower for k in ["knee", "torso", "lean", "depth", "elbow", "swing", "momentum", "back", "shallow"]):
        category = "WARNING"
        priority = "MEDIUM"
        status_label = "ADJUST FORM"
    else:
        category = "ACTIVE"
        priority = "LOW"
        status_label = "IN MOTION"

    # Default Context
    body_focus = "FULL_BODY"
    focus_label = "FULL BODY — OPTIMAL ALIGNMENT"
    action = "Maintain current cadence, alignment, and controlled lockout."
    what_to_do = "Replicate current movement pattern on every repetition."
    why_it_matters = "Postural consistency builds neuromuscular memory and injury resilience."
    next_rep_focus = "Maintain your current form. Focus on controlled, rhythmic movement."

    # Contextual refinement based on biomechanical keywords
    if category == "CORRECT":
        # Validated rep or optimal posture confirmed
        pass
    elif "knee" in msg_lower or "valgus" in msg_lower:
        body_focus = "KNEES"
        focus_label = "KNEE ALIGNMENT — TRACK OVER TOES"
        action = "Drive knees outward over your second toes; prevent inward knee cave."
        what_to_do = "Keep your knees tracking directly over your foot angle during ascent & descent."
        why_it_matters = "Knee valgus causes medial joint strain and reduces glute activation."
        next_rep_focus = "Spread the floor with your feet to keep knees stable and aligned."

    elif any(k in msg_lower for k in ["torso", "chest", "back", "spine"]) or ("lean" in msg_lower and "clean" not in msg_lower):
        body_focus = "SPINE"
        focus_label = "SPINE & TORSO — ATTENTION REQUIRED"
        action = "Elevate chest, pack lats, and maintain a rigid neutral lumbar spine."
        what_to_do = "Keep your chest proud and resist excessive forward torso inclination."
        why_it_matters = "Excessive torso lean shifts shear stress directly onto lumbar vertebrae."
        next_rep_focus = "Brace core muscles tightly and maintain eye-level gaze."

    elif any(k in msg_lower for k in ["depth", "shallow", "parallel"]):
        body_focus = "HIPS"
        focus_label = "HIP DEPTH — EXPAND RANGE OF MOTION"
        action = "Lower with controlled tempo until hip crease reaches knee parallel."
        what_to_do = "Reach full target depth before initiating upward drive."
        why_it_matters = "Full range of motion ensures maximal hamstring and glute recruitment."
        next_rep_focus = "Control your descent tempo and achieve parallel depth."

    elif any(k in msg_lower for k in ["elbow", "swing", "momentum"]):
        body_focus = "ELBOWS"
        focus_label = "ELBOW STABILITY — ELIMINATE SWAY"
        action = "Pin elbows firmly against ribcage and eliminate torso momentum."
        what_to_do = "Keep elbows locked as a fixed rotational pivot against your sides."
        why_it_matters = "Swinging arms forward shifts tension off biceps onto front deltoids."
        next_rep_focus = "Slow down cadence and squeeze at peak contraction."

    elif "sitting" in msg_lower:
        body_focus = "HIPS"
        focus_label = "ACTIVE TENSION — NO PASSIVE REST"
        action = "Do not rest body weight on chair or bench; maintain active tension."
        what_to_do = "Touch lightly and immediately drive back up without resting."
        why_it_matters = "Passive sitting relaxes stabilizing muscles and breaks kinetic tension."
        next_rep_focus = "Perform touch-and-go squats with constant quad tension."

    elif any(k in msg_lower for k in ["calibrat", "steady", "countdown"]):
        body_focus = "FULL_BODY"
        focus_label = "CALIBRATING — STAND CLEAR IN FRAME"
        action = "Position full body in camera frame and hold steady."
        what_to_do = "Allow YOLOv8 computer vision to register anatomical landmarks."
        why_it_matters = "Accurate baseline calibration ensures precision angle tracking."
        next_rep_focus = "Prepare for exercise rep 1 with balanced stance."

    return {
        "category": category,
        "status_label": status_label,
        "observation": feedback_msg or "Awaiting movement detection...",
        "action": action,
        "priority": priority,
        "body_focus": body_focus,
        "focus_label": focus_label,
        "what_to_do": what_to_do,
        "why_it_matters": why_it_matters,
        "next_rep_focus": next_rep_focus
    }

