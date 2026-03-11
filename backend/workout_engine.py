"""
Workout Engine - Rule-based workout generation system.
Determines training mode, selects exercises, and builds weekly plans.
All decisions are explainable and traceable.
"""

import random
from exercise_library import EXERCISES, get_exercises


# ──────────────────── MODE DETERMINATION ────────────────────
def determine_training_mode(adherence, recovery_level):
    """
    Determine training mode using rule-based logic.
    Rules:
      - Performance: adherence >= 80 AND recovery == 'high'
      - Recovery: adherence < 50 OR recovery == 'low'
      - Balanced: everything else
    Returns: (mode, explanation)
    """
    if adherence >= 80 and recovery_level == "high":
        return "performance", (
            f"Your high adherence ({adherence}%) combined with high recovery "
            "indicates you can handle increased training volume and intensity."
        )
    elif adherence < 50 or recovery_level == "low":
        reason_parts = []
        if adherence < 50:
            reason_parts.append(f"low adherence ({adherence}%)")
        if recovery_level == "low":
            reason_parts.append("low self-reported recovery")
        return "recovery", (
            f"Your {' and '.join(reason_parts)} suggest a recovery-focused approach "
            "to prevent overtraining and build sustainable habits."
        )
    else:
        return "balanced", (
            f"Your adherence ({adherence}%) and {recovery_level} recovery "
            "suggest a balanced training approach with moderate volume."
        )


# ──────────────────── SPLIT DETERMINATION ────────────────────
def determine_weekly_split(goal, experience, available_time):
    """
    Determine the weekly training split based on goal, experience, and time.
    Returns: list of day configs [{day, name, categories, is_rest}]
    """
    splits = {
        "muscle_gain": {
            "beginner": [
                {"day": 1, "name": "Full Body A", "categories": ["push", "legs", "core"], "is_rest": False},
                {"day": 2, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 3, "name": "Full Body B", "categories": ["pull", "legs", "core"], "is_rest": False},
                {"day": 4, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 5, "name": "Full Body C", "categories": ["push", "pull", "conditioning"], "is_rest": False},
                {"day": 6, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
            "intermediate": [
                {"day": 1, "name": "Upper Body Push", "categories": ["push", "core"], "is_rest": False},
                {"day": 2, "name": "Lower Body", "categories": ["legs", "conditioning"], "is_rest": False},
                {"day": 3, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 4, "name": "Upper Body Pull", "categories": ["pull", "core"], "is_rest": False},
                {"day": 5, "name": "Lower Body + Core", "categories": ["legs", "core"], "is_rest": False},
                {"day": 6, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
            "advanced": [
                {"day": 1, "name": "Push Day", "categories": ["push", "core"], "is_rest": False},
                {"day": 2, "name": "Pull Day", "categories": ["pull", "core"], "is_rest": False},
                {"day": 3, "name": "Legs Day", "categories": ["legs", "conditioning"], "is_rest": False},
                {"day": 4, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 5, "name": "Upper Hypertrophy", "categories": ["push", "pull"], "is_rest": False},
                {"day": 6, "name": "Lower Hypertrophy", "categories": ["legs", "core", "conditioning"], "is_rest": False},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
        },
        "fat_loss": {
            "beginner": [
                {"day": 1, "name": "Full Body + Cardio", "categories": ["push", "legs", "conditioning"], "is_rest": False},
                {"day": 2, "name": "Rest / Active Recovery", "categories": [], "is_rest": True},
                {"day": 3, "name": "Full Body + Core", "categories": ["pull", "legs", "core"], "is_rest": False},
                {"day": 4, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 5, "name": "Conditioning + Core", "categories": ["conditioning", "core", "push"], "is_rest": False},
                {"day": 6, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
            "intermediate": [
                {"day": 1, "name": "Upper Body + HIIT", "categories": ["push", "conditioning"], "is_rest": False},
                {"day": 2, "name": "Lower Body", "categories": ["legs", "core"], "is_rest": False},
                {"day": 3, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 4, "name": "Full Body Circuit", "categories": ["pull", "legs", "conditioning"], "is_rest": False},
                {"day": 5, "name": "Core + Conditioning", "categories": ["core", "conditioning", "push"], "is_rest": False},
                {"day": 6, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
            "advanced": [
                {"day": 1, "name": "Push + HIIT", "categories": ["push", "conditioning"], "is_rest": False},
                {"day": 2, "name": "Pull + Core", "categories": ["pull", "core"], "is_rest": False},
                {"day": 3, "name": "Legs + Conditioning", "categories": ["legs", "conditioning"], "is_rest": False},
                {"day": 4, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 5, "name": "Full Body Circuit", "categories": ["push", "pull", "conditioning"], "is_rest": False},
                {"day": 6, "name": "Legs + Core", "categories": ["legs", "core"], "is_rest": False},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
        },
        "general_fitness": {
            "beginner": [
                {"day": 1, "name": "Full Body A", "categories": ["push", "legs", "core"], "is_rest": False},
                {"day": 2, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 3, "name": "Full Body B", "categories": ["pull", "conditioning", "core"], "is_rest": False},
                {"day": 4, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 5, "name": "Full Body C", "categories": ["push", "legs", "conditioning"], "is_rest": False},
                {"day": 6, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
            "intermediate": [
                {"day": 1, "name": "Upper Body", "categories": ["push", "pull"], "is_rest": False},
                {"day": 2, "name": "Lower Body + Core", "categories": ["legs", "core"], "is_rest": False},
                {"day": 3, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 4, "name": "Full Body + Conditioning", "categories": ["push", "pull", "conditioning"], "is_rest": False},
                {"day": 5, "name": "Legs + Core", "categories": ["legs", "core", "conditioning"], "is_rest": False},
                {"day": 6, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
            "advanced": [
                {"day": 1, "name": "Push + Core", "categories": ["push", "core"], "is_rest": False},
                {"day": 2, "name": "Pull + Conditioning", "categories": ["pull", "conditioning"], "is_rest": False},
                {"day": 3, "name": "Legs", "categories": ["legs", "core"], "is_rest": False},
                {"day": 4, "name": "Rest Day", "categories": [], "is_rest": True},
                {"day": 5, "name": "Upper Body Mix", "categories": ["push", "pull"], "is_rest": False},
                {"day": 6, "name": "Conditioning + Core", "categories": ["conditioning", "legs", "core"], "is_rest": False},
                {"day": 7, "name": "Rest Day", "categories": [], "is_rest": True},
            ],
        },
    }

    return splits.get(goal, splits["general_fitness"]).get(experience, splits["general_fitness"]["beginner"])


# ──────────────────── EXERCISE SELECTION ────────────────────
def get_max_exercises(mode, available_time):
    """Determine max exercises per session based on mode and time."""
    time_limits = {"20-30": 4, "40-50": 5, "60+": 6}
    mode_limits = {"performance": 6, "balanced": 5, "recovery": 4}
    return min(time_limits.get(available_time, 5), mode_limits.get(mode, 5))


def get_min_exercises(mode):
    """Minimum exercises per non-rest day."""
    return 3


def select_day_exercises(categories, equipment, mode, available_time, experience, used_ids, seed_val):
    """
    Select exercises for a single training day.
    Ensures variety (no repeats across days) and respects constraints.
    """
    rng = random.Random(seed_val)
    max_ex = get_max_exercises(mode, available_time)
    min_ex = get_min_exercises(mode)
    selected = []
    explanations = []

    for cat in categories:
        pool = get_exercises(equipment, category=cat)
        # Filter out already-used exercises for variety
        available = [e for e in pool if e["id"] not in used_ids]
        if not available:
            available = pool  # Fallback if all used

        # Filter by difficulty for beginners in recovery mode
        if experience == "beginner" or mode == "recovery":
            preferred = [e for e in available if e["difficulty"] in ("beginner", "intermediate")]
            if preferred:
                available = preferred

        # Pick primary first, then accessory
        primaries = [e for e in available if e["role"] == "primary"]
        accessories = [e for e in available if e["role"] == "accessory"]

        rng.shuffle(primaries)
        rng.shuffle(accessories)

        # Select 1-2 primaries per category
        for ex in primaries[:2]:
            if len(selected) >= max_ex:
                break
            selected.append(ex)
            used_ids.add(ex["id"])
            explanations.append(
                f"'{ex['name']}' selected as primary {cat} exercise for {ex['muscle_group']}"
            )

        # Fill with accessories if room
        for ex in accessories[:1]:
            if len(selected) >= max_ex:
                break
            selected.append(ex)
            used_ids.add(ex["id"])
            explanations.append(
                f"'{ex['name']}' added as accessory {cat} movement"
            )

    # Ensure minimum exercises
    if len(selected) < min_ex:
        all_pool = get_exercises(equipment)
        extra = [e for e in all_pool if e["id"] not in used_ids]
        rng.shuffle(extra)
        while len(selected) < min_ex and extra:
            ex = extra.pop(0)
            selected.append(ex)
            used_ids.add(ex["id"])

    # Apply mode-based volume adjustments
    for ex in selected:
        ex_copy = dict(ex)
        if mode == "performance":
            ex_copy["sets"] = ex["sets"] + 1
            ex_copy["why_chosen"] = f"[Rule-Based] {ex['name']} - Volume increased (+1 set) due to Performance Mode."
        elif mode == "recovery":
            ex_copy["sets"] = max(2, ex["sets"] - 1)
            ex_copy["why_chosen"] = f"[Rule-Based] {ex['name']} - Volume reduced (-1 set) for Recovery Mode."
        else:
            ex_copy["why_chosen"] = f"[Rule-Based] {ex['name']} - Standard volume for Balanced Mode."
        selected[selected.index(ex)] = ex_copy

    return selected, explanations


# ──────────────────── WEEKLY PLAN GENERATION ────────────────────
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def generate_weekly_workout(user_data, ml_adjustments=None):
    """
    Generate a complete 7-day workout plan.
    Uses rule-based logic with optional ML-influenced adjustments.
    """
    adherence = user_data["weekly_adherence"]
    recovery = user_data["recovery_level"]
    goal = user_data["fitness_goal"]
    experience = user_data["experience_level"]
    equipment = user_data["equipment"]
    available_time = user_data["available_time"]

    # Determine training mode
    mode, mode_explanation = determine_training_mode(adherence, recovery)

    # Apply ML adjustments if provided
    if ml_adjustments:
        if ml_adjustments.get("force_recovery") and mode != "recovery":
            mode = "recovery"
            mode_explanation += " [ML Override: Cluster pattern suggests recovery-focus benefits]"
        if ml_adjustments.get("boost_volume") and mode == "balanced":
            mode = "performance"
            mode_explanation += " [ML Insight: Similar users benefited from higher volume]"

    # Get weekly split
    split = determine_weekly_split(goal, experience, available_time)

    # Build weekly plan
    weekly_plan = []
    used_exercise_ids = set()
    seed_base = hash(f"{user_data.get('age', 25)}{adherence}{goal}{equipment}")

    for day_config in split:
        day_num = day_config["day"]
        if day_config["is_rest"]:
            weekly_plan.append({
                "day": day_num,
                "day_name": DAY_NAMES[day_num - 1],
                "workout_name": day_config["name"],
                "is_rest_day": True,
                "exercises": [],
                "explanation": "Rest day for muscle recovery and adaptation. "
                               "Active recovery like walking or light stretching recommended."
            })
        else:
            exercises, explanations = select_day_exercises(
                categories=day_config["categories"],
                equipment=equipment,
                mode=mode,
                available_time=available_time,
                experience=experience,
                used_ids=used_exercise_ids,
                seed_val=seed_base + day_num
            )
            weekly_plan.append({
                "day": day_num,
                "day_name": DAY_NAMES[day_num - 1],
                "workout_name": day_config["name"],
                "is_rest_day": False,
                "exercises": exercises,
                "explanation": f"{day_config['name']} targeting {', '.join(day_config['categories'])}. "
                               f"Mode: {mode.title()} | {len(exercises)} exercises selected."
            })

    return {
        "mode": mode,
        "mode_label": f"{mode.title()} Mode",
        "mode_explanation": mode_explanation,
        "weekly_plan": weekly_plan
    }
