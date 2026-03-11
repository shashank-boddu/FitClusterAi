"""
Diet Engine - Rule-based diet plan generator.
Calculates BMR, TDEE, macros and generates 7-day meal plans with Indian cuisine.
"""

import random
from diet_library import get_foods_by_preference


# ──────────────────── BMR & TDEE CALCULATION ────────────────────
def calculate_bmr(age, gender, height_cm, weight_kg):
    """
    Mifflin-St Jeor equation for Basal Metabolic Rate.
    Male: (10 * weight) + (6.25 * height) - (5 * age) + 5
    Female: (10 * weight) + (6.25 * height) - (5 * age) - 161
    """
    if gender == "male":
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161


def calculate_tdee(bmr, experience_level):
    """Estimate TDEE using activity multiplier based on experience level."""
    multipliers = {
        "beginner": 1.4,     # Light activity
        "intermediate": 1.6,  # Moderate activity
        "advanced": 1.8       # High activity
    }
    return bmr * multipliers.get(experience_level, 1.5)


def adjust_calories_for_goal(tdee, goal):
    """
    Adjust calorie target based on fitness goal.
    Muscle gain: +300 surplus, Fat loss: -400 deficit, General: maintenance
    """
    adjustments = {
        "muscle_gain": 300,
        "fat_loss": -400,
        "general_fitness": 0
    }
    return round(tdee + adjustments.get(goal, 0))


def calculate_macros(target_calories, goal, weight_kg):
    """
    Calculate macro targets in grams.
    Protein: based on goal and bodyweight.
    Fat: ~25-30% of calories. Carbs: remainder.
    """
    protein_multipliers = {
        "muscle_gain": 2.0,     # g per kg bodyweight
        "fat_loss": 1.8,
        "general_fitness": 1.5
    }
    protein_g = round(weight_kg * protein_multipliers.get(goal, 1.6))
    fat_g = round((target_calories * 0.28) / 9)
    carbs_g = round((target_calories - (protein_g * 4) - (fat_g * 9)) / 4)
    carbs_g = max(carbs_g, 50)  # Minimum carbs

    return {
        "protein": protein_g,
        "carbs": carbs_g,
        "fat": fat_g,
        "protein_calories": protein_g * 4,
        "carbs_calories": carbs_g * 4,
        "fat_calories": fat_g * 9,
    }


# ──────────────────── MEAL PLAN GENERATION ────────────────────
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ──────────────────── SUPPLEMENT FOODS ────────────────────
# These are add-on items to bridge calorie/protein gaps in meal plans
SUPPLEMENTS_VEG = [
    {"id": "glass_milk", "name": "Glass of Warm Milk", "calories": 150, "protein": 8, "carbs": 12, "fat": 8, "cooking_time": "2 mins", "portion_size": "1 glass (250ml)", "recipe": ["Warm 250ml full-fat milk", "Add a pinch of turmeric or cardamom", "Serve warm"]},
    {"id": "banana", "name": "Banana", "calories": 105, "protein": 1, "carbs": 27, "fat": 0, "cooking_time": "0 mins", "portion_size": "1 medium banana", "recipe": ["Peel and eat fresh", "Best consumed post-workout or as energy snack"]},
    {"id": "peanut_butter_toast", "name": "Peanut Butter on Toast", "calories": 260, "protein": 10, "carbs": 28, "fat": 14, "cooking_time": "3 mins", "portion_size": "2 slices + 2 tbsp PB", "recipe": ["Toast 2 slices of multigrain bread", "Spread 1 tbsp peanut butter on each slice", "Optional: add sliced banana on top"]},
    {"id": "curd_bowl", "name": "Curd with Honey", "calories": 130, "protein": 6, "carbs": 18, "fat": 4, "cooking_time": "0 mins", "portion_size": "1 bowl (200g)", "recipe": ["Take 200g fresh curd in a bowl", "Drizzle 1 tsp honey", "Mix well and serve chilled"]},
    {"id": "extra_roti", "name": "Whole Wheat Roti (Extra)", "calories": 120, "protein": 4, "carbs": 22, "fat": 3, "cooking_time": "5 mins", "portion_size": "1 roti", "recipe": ["Roll wheat dough into thin disc", "Cook on hot tawa with light ghee", "Serve hot alongside main curry"]},
    {"id": "extra_rice", "name": "Steamed Brown Rice (Extra)", "calories": 215, "protein": 5, "carbs": 45, "fat": 2, "cooking_time": "10 mins", "portion_size": "1 cup cooked", "recipe": ["Cook 1/2 cup brown rice in 1 cup water", "Simmer until water absorbed", "Fluff with fork and serve"]},
    {"id": "sattu_drink", "name": "Sattu Sharbat", "calories": 180, "protein": 12, "carbs": 25, "fat": 3, "cooking_time": "3 mins", "portion_size": "1 glass (300ml)", "recipe": ["Mix 3 tbsp sattu powder in cold water", "Add lemon juice, black salt, roasted cumin", "Stir well and serve chilled"]},
    {"id": "chana_dal_bowl", "name": "Roasted Chana Dal", "calories": 170, "protein": 11, "carbs": 24, "fat": 4, "cooking_time": "0 mins", "portion_size": "1 cup (80g)", "recipe": ["Take 80g roasted chana dal", "Season with chaat masala and black salt", "Consume as high-protein snack"]},
    {"id": "paneer_slice", "name": "Paneer Cubes (Grilled)", "calories": 200, "protein": 14, "carbs": 3, "fat": 15, "cooking_time": "8 mins", "portion_size": "100g", "recipe": ["Cut 100g paneer into cubes", "Season with salt, pepper, chaat masala", "Grill or pan-fry until golden on each side"]},
    {"id": "lassi", "name": "Sweet Lassi", "calories": 180, "protein": 7, "carbs": 26, "fat": 6, "cooking_time": "3 mins", "portion_size": "1 glass (300ml)", "recipe": ["Blend 200g curd with 100ml water", "Add sugar and cardamom powder", "Blend until frothy, serve cold"]},
]

SUPPLEMENTS_NONVEG = SUPPLEMENTS_VEG + [
    {"id": "boiled_eggs_2", "name": "Boiled Eggs (2)", "calories": 155, "protein": 13, "carbs": 1, "fat": 11, "cooking_time": "10 mins", "portion_size": "2 eggs", "recipe": ["Boil 2 eggs for 8-10 minutes", "Cool and peel", "Season with salt and pepper"]},
    {"id": "chicken_salad_side", "name": "Grilled Chicken Side", "calories": 180, "protein": 26, "carbs": 2, "fat": 8, "cooking_time": "12 mins", "portion_size": "100g chicken breast", "recipe": ["Season 100g chicken breast with salt, pepper, lemon", "Grill for 5-6 minutes each side", "Slice and serve alongside main meal"]},
    {"id": "egg_whites_3", "name": "Boiled Egg Whites (3)", "calories": 50, "protein": 12, "carbs": 0, "fat": 0, "cooking_time": "10 mins", "portion_size": "3 egg whites", "recipe": ["Boil 3 eggs for 10 minutes", "Peel and discard yolks", "Season whites with pepper and salt"]},
]


def _copy_food(food):
    """Create a shallow copy to avoid mutating the original library."""
    return dict(food)


def _meal_cals(meal):
    return sum(f["calories"] for f in meal["foods"])


def _meal_protein(meal):
    return sum(f["protein"] for f in meal["foods"])


def _get_supplements(is_veg, rng, day_idx):
    """Get a shuffled list of supplement items for calorie/protein gap filling."""
    pool = list(SUPPLEMENTS_VEG if is_veg else SUPPLEMENTS_NONVEG)
    # Rotate pool based on day to ensure variety across days
    rotation = day_idx * 3
    pool = pool[rotation % len(pool):] + pool[:rotation % len(pool)]
    rng.shuffle(pool)
    return [dict(s) for s in pool]


def generate_weekly_diet(user_data):
    """
    Generate a 7-day diet plan with different foods each day.
    Respects veg/non-veg preference and meets calorie/protein targets.
    """
    age = user_data["age"]
    gender = user_data["gender"]
    height = user_data["height"]
    weight = user_data["weight"]
    goal = user_data["fitness_goal"]
    experience = user_data["experience_level"]
    is_veg = user_data["diet_preference"] == "vegetarian"

    # Calculate nutritional targets
    bmr = calculate_bmr(age, gender, height, weight)
    tdee = calculate_tdee(bmr, experience)
    target_calories = adjust_calories_for_goal(tdee, goal)
    macros = calculate_macros(target_calories, goal, weight)

    # Get food pools by meal type
    breakfasts = get_foods_by_preference(is_veg, "breakfast")
    lunches = get_foods_by_preference(is_veg, "lunch")
    snacks = get_foods_by_preference(is_veg, "snack")
    dinners = get_foods_by_preference(is_veg, "dinner")

    # Seed for reproducibility based on user profile
    seed = hash(f"{age}{gender}{height}{weight}{goal}")
    rng = random.Random(seed)

    rng.shuffle(breakfasts)
    rng.shuffle(lunches)
    rng.shuffle(snacks)
    rng.shuffle(dinners)

    weekly_diet = []
    for day_idx in range(7):
        # Pick different foods for each day (cycle if not enough)
        bf = breakfasts[day_idx % len(breakfasts)]
        ln = lunches[day_idx % len(lunches)]
        ms = snacks[day_idx % len(snacks)]
        es = snacks[(day_idx + 1) % len(snacks)] if len(snacks) > 1 else snacks[0]
        dn = dinners[day_idx % len(dinners)]

        # Ensure mid-morning and evening snacks are different
        if es["id"] == ms["id"] and len(snacks) > 2:
            es = snacks[(day_idx + 2) % len(snacks)]

        # Build base meals
        meals = [
            {"meal_type": "Breakfast", "foods": [_copy_food(bf)]},
            {"meal_type": "Mid-Morning Snack", "foods": [_copy_food(ms)]},
            {"meal_type": "Lunch", "foods": [_copy_food(ln)]},
            {"meal_type": "Evening Snack", "foods": [_copy_food(es)]},
            {"meal_type": "Dinner", "foods": [_copy_food(dn)]},
        ]

        # Calculate base totals
        base_calories = sum(_meal_cals(m) for m in meals)
        base_protein = sum(_meal_protein(m) for m in meals)

        # Fill gap to meet calorie & protein target with supplements
        calorie_gap = target_calories - base_calories
        protein_gap = macros["protein"] - base_protein

        # Only add supplements when there's a meaningful deficit (>150 kcal)
        if calorie_gap > 150:
            supplements = _get_supplements(is_veg, rng, day_idx)
            # Sort by calories ascending so we pick smaller items for small gaps
            supplements.sort(key=lambda s: s["calories"])

            main_meal_indices = [0, 2, 4]  # breakfast, lunch, dinner
            supp_idx = 0
            while calorie_gap > 150 and supp_idx < len(supplements):
                supp = supplements[supp_idx]
                # Only add if it doesn't overshoot target by more than 80 kcal
                if supp["calories"] <= calorie_gap + 80:
                    target_meal = main_meal_indices[supp_idx % len(main_meal_indices)]
                    meals[target_meal]["foods"].append(supp)
                    calorie_gap -= supp["calories"]
                    protein_gap -= supp["protein"]
                supp_idx += 1

            # Add pre-bed meal only for large remaining gaps (>300 kcal)
            if calorie_gap > 300:
                prebed_items = []
                remaining_supps = [s for s in supplements[supp_idx:]]
                for s in remaining_supps:
                    if calorie_gap <= 150:
                        break
                    if s["calories"] <= calorie_gap + 80:
                        prebed_items.append(s)
                        calorie_gap -= s["calories"]
                if prebed_items:
                    meals.append({"meal_type": "Pre-Bed Snack", "foods": prebed_items})

        # Calculate final day totals
        day_calories = sum(_meal_cals(m) for m in meals)
        day_protein = sum(_meal_protein(m) for m in meals)
        day_carbs = sum(sum(f["carbs"] for f in m["foods"]) for m in meals)
        day_fat = sum(sum(f["fat"] for f in m["foods"]) for m in meals)

        weekly_diet.append({
            "day": day_idx + 1,
            "day_name": DAY_NAMES[day_idx],
            "meals": meals,
            "total_calories": day_calories,
            "total_protein": day_protein,
            "total_carbs": day_carbs,
            "total_fat": day_fat,
        })

    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "target_calories": target_calories,
        "macros": macros,
        "weekly_diet": weekly_diet,
        "explanation": (
            f"BMR calculated at {round(bmr)} kcal using Mifflin-St Jeor equation. "
            f"TDEE estimated at {round(tdee)} kcal ({experience} activity level). "
            f"Target: {target_calories} kcal/day "
            f"({'surplus for muscle gain' if goal == 'muscle_gain' else 'deficit for fat loss' if goal == 'fat_loss' else 'maintenance'}). "
            f"Protein target: {macros['protein']}g ({macros['protein'] / weight:.1f}g/kg bodyweight)."
        )
    }
