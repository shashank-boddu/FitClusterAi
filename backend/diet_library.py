"""
Indian Diet Library - Comprehensive food database with nutritional data and recipes.
Includes vegetarian and non-vegetarian options with macros, recipes, and portion info.
All foods are Indian cuisine focused for cultural relevance.
"""

FOODS = [
    # ===== BREAKFAST - VEGETARIAN =====
    {
        "id": "masala_oats",
        "name": "Masala Oats",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 280,
        "protein": 10,
        "carbs": 45,
        "fat": 8,
        "cooking_time": "15 mins",
        "portion_size": "1 bowl (200g)",
        "recipe": [
            "Heat 1 tsp oil in a pan over medium heat",
            "Add 1/2 tsp mustard seeds and 5-6 curry leaves, let them splutter",
            "Add 1 chopped onion and 1 chopped green chili, saute for 2 mins",
            "Add 1 chopped tomato and cook until soft",
            "Add 1 cup rolled oats and 2 cups water",
            "Add salt, turmeric, and red chili powder to taste",
            "Cook for 5-7 minutes stirring occasionally",
            "Garnish with fresh coriander leaves and serve hot"
        ]
    },
    {
        "id": "moong_dal_cheela",
        "name": "Moong Dal Cheela",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 220,
        "protein": 14,
        "carbs": 30,
        "fat": 6,
        "cooking_time": "20 mins",
        "portion_size": "3 cheelas",
        "recipe": [
            "Soak 1 cup moong dal for 4 hours, drain and grind into smooth batter",
            "Add chopped onions, green chili, ginger, salt, and coriander",
            "Heat a non-stick pan and spread a ladleful of batter in circular motion",
            "Drizzle oil around the edges and cook until golden",
            "Flip and cook the other side for 1-2 minutes",
            "Serve hot with green chutney and curd"
        ]
    },
    {
        "id": "poha",
        "name": "Vegetable Poha",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 250,
        "protein": 6,
        "carbs": 42,
        "fat": 7,
        "cooking_time": "15 mins",
        "portion_size": "1 plate (200g)",
        "recipe": [
            "Wash 2 cups flattened rice (poha) and drain well",
            "Heat oil, add mustard seeds, curry leaves, and peanuts",
            "Add chopped onions and green chili, saute until translucent",
            "Add turmeric, salt, and a pinch of sugar",
            "Add the washed poha and mix gently",
            "Cook on low heat for 3-4 minutes",
            "Squeeze fresh lemon juice and garnish with coriander and sev"
        ]
    },
    {
        "id": "idli_sambar",
        "name": "Idli with Sambar",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 300,
        "protein": 12,
        "carbs": 52,
        "fat": 5,
        "cooking_time": "30 mins (batter pre-made)",
        "portion_size": "4 idlis + 1 bowl sambar",
        "recipe": [
            "Pour fermented idli batter into greased idli molds",
            "Steam for 10-12 minutes until firm",
            "For sambar: boil 1/2 cup toor dal until soft",
            "In a pot, cook chopped drumstick, carrot, and onion in tamarind water",
            "Add sambar powder, salt, and turmeric",
            "Mix in boiled dal and simmer for 10 minutes",
            "Temper with mustard seeds, curry leaves, and dried red chili",
            "Serve idlis hot with sambar and coconut chutney"
        ]
    },
    {
        "id": "besan_chilla",
        "name": "Besan Chilla",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 200,
        "protein": 12,
        "carbs": 22,
        "fat": 8,
        "cooking_time": "10 mins",
        "portion_size": "2 chillas",
        "recipe": [
            "Mix 1 cup besan (gram flour) with water to make smooth batter",
            "Add chopped onions, tomatoes, green chili, and coriander",
            "Season with salt, turmeric, and ajwain",
            "Heat a non-stick pan and spread batter thinly",
            "Cook on medium heat until edges lift, then flip",
            "Serve hot with mint chutney or ketchup"
        ]
    },
    {
        "id": "paneer_paratha",
        "name": "Paneer Paratha",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 350,
        "protein": 16,
        "carbs": 38,
        "fat": 15,
        "cooking_time": "25 mins",
        "portion_size": "2 parathas",
        "recipe": [
            "Grate 150g paneer and mix with chopped onion, green chili, coriander",
            "Add salt, cumin powder, and amchur to the filling",
            "Take wheat dough balls and roll into small discs",
            "Place filling in center, seal edges, and roll gently",
            "Cook on hot tawa with ghee on both sides until golden brown",
            "Serve hot with curd and pickle"
        ]
    },
    {
        "id": "upma",
        "name": "Vegetable Upma",
        "meal_type": "breakfast",
        "is_veg": True,
        "calories": 260,
        "protein": 8,
        "carbs": 40,
        "fat": 8,
        "cooking_time": "15 mins",
        "portion_size": "1 bowl (200g)",
        "recipe": [
            "Dry roast 1 cup rava (semolina) until golden, set aside",
            "Heat oil, add mustard seeds, urad dal, chana dal, and curry leaves",
            "Add chopped onion, green chili, ginger and saute",
            "Add chopped carrots, peas, and beans",
            "Pour 2.5 cups water, add salt and bring to boil",
            "Slowly add roasted rava while stirring continuously",
            "Cook on low heat for 3-4 minutes until water is absorbed",
            "Garnish with lemon juice and coriander leaves"
        ]
    },
    # ===== BREAKFAST - NON-VEG =====
    {
        "id": "egg_bhurji",
        "name": "Egg Bhurji with Toast",
        "meal_type": "breakfast",
        "is_veg": False,
        "calories": 320,
        "protein": 22,
        "carbs": 25,
        "fat": 16,
        "cooking_time": "10 mins",
        "portion_size": "3 eggs + 2 toast",
        "recipe": [
            "Heat oil in a pan, add cumin seeds",
            "Add chopped onion and green chili, cook until golden",
            "Add chopped tomato and cook for 2 minutes",
            "Add turmeric, salt, red chili powder",
            "Crack 3 eggs directly into the pan and scramble",
            "Cook on medium heat while stirring until eggs are done",
            "Garnish with coriander and serve with toasted bread"
        ]
    },
    {
        "id": "egg_white_omelette",
        "name": "Egg White Omelette",
        "meal_type": "breakfast",
        "is_veg": False,
        "calories": 180,
        "protein": 24,
        "carbs": 4,
        "fat": 6,
        "cooking_time": "8 mins",
        "portion_size": "4 egg whites + veggies",
        "recipe": [
            "Separate whites from 4 eggs into a bowl",
            "Add chopped bell peppers, onion, and mushroom",
            "Season with salt, pepper, and a pinch of oregano",
            "Heat non-stick pan with a spray of oil",
            "Pour egg white mixture and cook on medium heat",
            "Fold when edges set and serve with salad"
        ]
    },
    {
        "id": "boiled_eggs_toast",
        "name": "Boiled Eggs with Multigrain Toast",
        "meal_type": "breakfast",
        "is_veg": False,
        "calories": 290,
        "protein": 20,
        "carbs": 28,
        "fat": 12,
        "cooking_time": "12 mins",
        "portion_size": "3 eggs + 2 toast slices",
        "recipe": [
            "Boil 3 eggs in water for 8-10 minutes for hard boil",
            "Cool eggs in cold water and peel",
            "Toast 2 slices of multigrain bread until golden",
            "Slice eggs and arrange on toast",
            "Season with salt, pepper, and chaat masala",
            "Serve with a side of sliced cucumber and tomato"
        ]
    },
    # ===== LUNCH - VEGETARIAN =====
    {
        "id": "dal_tadka_rice",
        "name": "Dal Tadka with Brown Rice",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 420,
        "protein": 18,
        "carbs": 65,
        "fat": 10,
        "cooking_time": "30 mins",
        "portion_size": "1 bowl dal + 1 cup rice",
        "recipe": [
            "Wash and pressure cook 1 cup toor dal with turmeric for 3 whistles",
            "In a pan, heat ghee and add cumin seeds, garlic, and dried red chili",
            "Add chopped onions and tomatoes, cook until soft",
            "Add red chili powder, coriander powder, and salt",
            "Pour cooked dal into the tadka and simmer for 10 minutes",
            "Cook 1 cup brown rice separately",
            "Garnish dal with fresh coriander and serve with rice"
        ]
    },
    {
        "id": "rajma_chawal",
        "name": "Rajma Chawal",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 450,
        "protein": 20,
        "carbs": 68,
        "fat": 10,
        "cooking_time": "45 mins (beans pre-soaked)",
        "portion_size": "1 bowl rajma + 1 cup rice",
        "recipe": [
            "Soak 1 cup rajma overnight and pressure cook until soft",
            "Heat oil, add cumin seeds and bay leaf",
            "Add onion paste and cook until golden brown",
            "Add ginger-garlic paste, cook for 2 minutes",
            "Add tomato puree, rajma masala, turmeric, and salt",
            "Add boiled rajma with cooking water and simmer 20 mins",
            "Mash a few beans for thick gravy consistency",
            "Serve hot over steamed basmati rice with onion rings"
        ]
    },
    {
        "id": "palak_paneer_roti",
        "name": "Palak Paneer with Roti",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 400,
        "protein": 22,
        "carbs": 40,
        "fat": 18,
        "cooking_time": "30 mins",
        "portion_size": "1 bowl palak paneer + 2 rotis",
        "recipe": [
            "Blanch 2 bunches of spinach and blend into smooth puree",
            "Cube 200g paneer and lightly fry until golden",
            "Heat oil, add cumin seeds, onion, ginger-garlic paste",
            "Add green chili and cook until onion is golden",
            "Add spinach puree, salt, garam masala, and cream",
            "Add paneer cubes and simmer for 5 minutes",
            "Make 2 rotis from whole wheat dough on hot tawa",
            "Serve palak paneer hot with rotis"
        ]
    },
    {
        "id": "chole_roti",
        "name": "Chole with Whole Wheat Roti",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 430,
        "protein": 18,
        "carbs": 60,
        "fat": 14,
        "cooking_time": "40 mins",
        "portion_size": "1 bowl chole + 2 rotis",
        "recipe": [
            "Soak 1 cup chickpeas overnight and pressure cook until tender",
            "Heat oil, add tea bag or tea water for dark color",
            "Saute onions until deep brown, add ginger-garlic paste",
            "Add chole masala, amchur, red chili powder, and salt",
            "Add boiled chickpeas with water and simmer for 20 minutes",
            "Adjust consistency and garnish with onion rings and lemon",
            "Serve with hot whole wheat rotis"
        ]
    },
    {
        "id": "veg_pulao",
        "name": "Vegetable Pulao with Raita",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 380,
        "protein": 10,
        "carbs": 58,
        "fat": 12,
        "cooking_time": "25 mins",
        "portion_size": "1 plate pulao + raita",
        "recipe": [
            "Wash and soak 1 cup basmati rice for 20 minutes",
            "Heat ghee, add whole spices (bay leaf, cloves, cinnamon)",
            "Add sliced onion, ginger-garlic paste and saute",
            "Add mixed vegetables (carrots, peas, beans, cauliflower)",
            "Add rice, salt, and 2 cups water",
            "Cook on low heat until rice is done (about 15 mins)",
            "For raita: mix curd with grated cucumber, cumin, and salt",
            "Fluff pulao with fork and serve with raita"
        ]
    },
    {
        "id": "paneer_bhurji_roti",
        "name": "Paneer Bhurji with Roti",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 410,
        "protein": 24,
        "carbs": 38,
        "fat": 20,
        "cooking_time": "20 mins",
        "portion_size": "1 bowl bhurji + 2 rotis",
        "recipe": [
            "Crumble 250g paneer into small pieces",
            "Heat oil, add cumin seeds and chopped onion",
            "Add green chili, ginger, and cook for 2 minutes",
            "Add chopped tomato, turmeric, red chili, and salt",
            "Add crumbled paneer and mix well",
            "Cook for 5 minutes on medium heat",
            "Add garam masala and fresh coriander",
            "Serve hot with whole wheat rotis"
        ]
    },
    {
        "id": "mixed_veg_roti",
        "name": "Mixed Veg Sabzi with Roti",
        "meal_type": "lunch",
        "is_veg": True,
        "calories": 350,
        "protein": 12,
        "carbs": 48,
        "fat": 12,
        "cooking_time": "25 mins",
        "portion_size": "1 bowl sabzi + 2 rotis",
        "recipe": [
            "Chop mixed vegetables (potato, carrot, beans, capsicum, peas)",
            "Heat oil, add cumin seeds and hing",
            "Add onion and ginger-garlic paste, cook until golden",
            "Add chopped tomato and all dry masalas (turmeric, coriander, chili)",
            "Add vegetables with a splash of water and cover",
            "Cook on medium heat for 15 minutes until vegetables are tender",
            "Garnish with coriander and serve with rotis"
        ]
    },
    # ===== LUNCH - NON-VEG =====
    {
        "id": "chicken_curry_rice",
        "name": "Chicken Curry with Steamed Rice",
        "meal_type": "lunch",
        "is_veg": False,
        "calories": 520,
        "protein": 38,
        "carbs": 55,
        "fat": 16,
        "cooking_time": "40 mins",
        "portion_size": "1 bowl curry + 1 cup rice",
        "recipe": [
            "Marinate 300g chicken pieces with curd, turmeric, and salt for 15 mins",
            "Heat oil, add whole spices (bay leaf, cloves, cardamom)",
            "Add sliced onion and cook until deep golden brown",
            "Add ginger-garlic paste and saute for 2 minutes",
            "Add tomato puree and cook until oil separates",
            "Add chicken pieces and seal on high heat",
            "Add water, cover, and cook on low heat for 20 minutes",
            "Finish with garam masala and coriander, serve with steamed rice"
        ]
    },
    {
        "id": "grilled_chicken_roti",
        "name": "Grilled Chicken Breast with Roti",
        "meal_type": "lunch",
        "is_veg": False,
        "calories": 420,
        "protein": 42,
        "carbs": 35,
        "fat": 12,
        "cooking_time": "25 mins",
        "portion_size": "200g chicken + 2 rotis",
        "recipe": [
            "Marinate 200g chicken breast with curd, lemon juice, ginger-garlic paste",
            "Add tandoori masala, salt, and a tsp of oil",
            "Let marinate for at least 30 minutes",
            "Grill on medium-high heat for 6-7 minutes each side",
            "Internal temperature should reach 165F/74C",
            "Rest for 5 minutes before slicing",
            "Serve with hot rotis and mint chutney"
        ]
    },
    {
        "id": "fish_curry_rice",
        "name": "Fish Curry with Rice",
        "meal_type": "lunch",
        "is_veg": False,
        "calories": 440,
        "protein": 35,
        "carbs": 50,
        "fat": 14,
        "cooking_time": "30 mins",
        "portion_size": "200g fish + 1 cup rice",
        "recipe": [
            "Clean and cut 200g fish (rohu/surmai) into pieces",
            "Marinate with turmeric, salt, and lemon juice for 10 mins",
            "Heat mustard oil, add panch phoron or mustard seeds",
            "Add onion paste, ginger-garlic paste, and cook",
            "Add tomato, turmeric, red chili powder, and salt",
            "Add water and bring to simmer",
            "Gently add fish pieces and cook covered for 10-12 mins",
            "Serve with steamed rice and lemon wedge"
        ]
    },
    {
        "id": "chicken_biryani",
        "name": "Chicken Biryani",
        "meal_type": "lunch",
        "is_veg": False,
        "calories": 550,
        "protein": 32,
        "carbs": 65,
        "fat": 18,
        "cooking_time": "60 mins",
        "portion_size": "1 plate (350g)",
        "recipe": [
            "Marinate 300g chicken with curd, biryani masala, ginger-garlic paste",
            "Soak 1.5 cups basmati rice for 30 mins, parboil with whole spices",
            "Fry sliced onions until deep brown for birista",
            "Layer marinated chicken at bottom of heavy pot",
            "Add layer of parboiled rice on top",
            "Sprinkle saffron milk, fried onions, and mint leaves",
            "Seal pot with dough or tight lid (dum)",
            "Cook on lowest heat for 25 minutes, then let rest 10 mins before opening"
        ]
    },
    {
        "id": "keema_matar_roti",
        "name": "Keema Matar with Roti",
        "meal_type": "lunch",
        "is_veg": False,
        "calories": 480,
        "protein": 36,
        "carbs": 38,
        "fat": 20,
        "cooking_time": "30 mins",
        "portion_size": "1 bowl keema + 2 rotis",
        "recipe": [
            "Heat oil, add whole spices and chopped onion",
            "Cook until onion is golden, add ginger-garlic paste",
            "Add 250g chicken mince and cook on high heat breaking lumps",
            "Add tomato, all masalas (turmeric, coriander, cumin, garam masala)",
            "Add 1/2 cup green peas and salt",
            "Add a little water and cook covered for 15 minutes",
            "Garnish with fresh coriander and ginger juliennes",
            "Serve hot with whole wheat rotis"
        ]
    },
    # ===== SNACKS - VEGETARIAN =====
    {
        "id": "sprouts_salad",
        "name": "Sprouts Chaat Salad",
        "meal_type": "snack",
        "is_veg": True,
        "calories": 180,
        "protein": 12,
        "carbs": 28,
        "fat": 3,
        "cooking_time": "10 mins",
        "portion_size": "1 bowl (150g)",
        "recipe": [
            "Boil 1 cup mixed sprouts (moong, chana) for 5 minutes",
            "Drain and let cool",
            "Add chopped onion, tomato, cucumber, and green chili",
            "Squeeze lemon juice, add chaat masala and salt",
            "Toss well and garnish with fresh coriander",
            "Serve immediately for best crunch"
        ]
    },
    {
        "id": "roasted_chana",
        "name": "Roasted Chana Mix",
        "meal_type": "snack",
        "is_veg": True,
        "calories": 160,
        "protein": 10,
        "carbs": 22,
        "fat": 5,
        "cooking_time": "5 mins",
        "portion_size": "1 cup (100g)",
        "recipe": [
            "Take 1 cup roasted black chana",
            "Add chopped onion, tomato, and green chili",
            "Squeeze lemon juice and add chaat masala",
            "Toss everything together",
            "Optional: add a drizzle of tamarind chutney",
            "Serve as evening protein-rich snack"
        ]
    },
    {
        "id": "paneer_tikka",
        "name": "Paneer Tikka",
        "meal_type": "snack",
        "is_veg": True,
        "calories": 250,
        "protein": 18,
        "carbs": 8,
        "fat": 16,
        "cooking_time": "25 mins",
        "portion_size": "6-8 pieces",
        "recipe": [
            "Cut 200g paneer into cubes along with bell peppers and onion",
            "Make marinade: thick curd, besan, tikka masala, lemon juice, salt",
            "Coat paneer and vegetables in marinade for 30 minutes",
            "Thread onto skewers alternating paneer and vegetables",
            "Grill or bake at 200C for 15-18 minutes turning once",
            "Brush with butter and serve with mint chutney"
        ]
    },
    {
        "id": "mixed_nuts",
        "name": "Mixed Nuts & Seeds Trail Mix",
        "meal_type": "snack",
        "is_veg": True,
        "calories": 200,
        "protein": 7,
        "carbs": 10,
        "fat": 16,
        "cooking_time": "0 mins",
        "portion_size": "1 handful (35g)",
        "recipe": [
            "Take equal portions of almonds, walnuts, and cashews",
            "Add pumpkin seeds and sunflower seeds",
            "Add a few raisins or dried cranberries",
            "Mix everything together in a bowl",
            "Store in airtight container",
            "Consume 1 handful as mid-day protein boost"
        ]
    },
    {
        "id": "protein_smoothie",
        "name": "Banana Peanut Butter Smoothie",
        "meal_type": "snack",
        "is_veg": True,
        "calories": 280,
        "protein": 14,
        "carbs": 35,
        "fat": 12,
        "cooking_time": "5 mins",
        "portion_size": "1 glass (300ml)",
        "recipe": [
            "Add 1 ripe banana to blender",
            "Add 2 tbsp peanut butter and 1 cup cold milk",
            "Add 1 tbsp honey and a pinch of cinnamon",
            "Add 4-5 ice cubes",
            "Blend until smooth and creamy",
            "Pour into glass and serve immediately"
        ]
    },
    # ===== SNACKS - NON-VEG =====
    {
        "id": "boiled_egg_whites",
        "name": "Boiled Egg Whites with Pepper",
        "meal_type": "snack",
        "is_veg": False,
        "calories": 100,
        "protein": 20,
        "carbs": 2,
        "fat": 1,
        "cooking_time": "12 mins",
        "portion_size": "5 egg whites",
        "recipe": [
            "Boil 5 eggs in water for 10 minutes",
            "Cool in ice water and peel",
            "Remove yolks (save for other use or discard)",
            "Season egg whites with black pepper, salt, chaat masala",
            "Optionally add a squeeze of lemon",
            "High protein, low calorie post-workout snack"
        ]
    },
    {
        "id": "chicken_seekh_kebab",
        "name": "Chicken Seekh Kebab",
        "meal_type": "snack",
        "is_veg": False,
        "calories": 220,
        "protein": 28,
        "carbs": 6,
        "fat": 10,
        "cooking_time": "20 mins",
        "portion_size": "3 kebabs",
        "recipe": [
            "Mince 200g chicken breast or use chicken mince",
            "Add finely chopped onion, green chili, coriander, mint",
            "Add ginger-garlic paste, kebab masala, salt, and 1 egg",
            "Mix well and shape into cylinders on skewers",
            "Grill or pan-fry on medium heat for 4-5 mins each side",
            "Serve with green chutney and sliced onion rings"
        ]
    },
    {
        "id": "fish_tikka",
        "name": "Fish Tikka",
        "meal_type": "snack",
        "is_veg": False,
        "calories": 200,
        "protein": 30,
        "carbs": 5,
        "fat": 8,
        "cooking_time": "20 mins",
        "portion_size": "5-6 pieces",
        "recipe": [
            "Cut 200g boneless fish into chunks",
            "Make marinade: curd, besan, ajwain, tikka masala, lemon",
            "Coat fish pieces and refrigerate for 20 minutes",
            "Grill or air-fry at 200C for 12-15 minutes",
            "Turn once halfway through cooking",
            "Serve hot with mint chutney and onion rings"
        ]
    },
    # ===== DINNER - VEGETARIAN =====
    {
        "id": "khichdi",
        "name": "Moong Dal Khichdi",
        "meal_type": "dinner",
        "is_veg": True,
        "calories": 320,
        "protein": 14,
        "carbs": 52,
        "fat": 6,
        "cooking_time": "25 mins",
        "portion_size": "1 bowl (250g)",
        "recipe": [
            "Wash 1/2 cup rice and 1/2 cup moong dal together",
            "Heat ghee in pressure cooker, add cumin, hing, and turmeric",
            "Add rice-dal mixture with 3 cups water and salt",
            "Pressure cook for 3 whistles",
            "Let pressure release naturally",
            "Mash lightly for creamy consistency",
            "Temper with ghee, cumin seeds, and dried red chili",
            "Serve with pickle and papad"
        ]
    },
    {
        "id": "mushroom_curry_roti",
        "name": "Mushroom Masala with Roti",
        "meal_type": "dinner",
        "is_veg": True,
        "calories": 340,
        "protein": 14,
        "carbs": 42,
        "fat": 14,
        "cooking_time": "25 mins",
        "portion_size": "1 bowl + 2 rotis",
        "recipe": [
            "Clean and slice 200g button mushrooms",
            "Heat oil, add cumin seeds and chopped onion",
            "Add ginger-garlic paste and green chili",
            "Add tomato puree and cook until oil separates",
            "Add turmeric, coriander powder, red chili powder, garam masala",
            "Add mushrooms and cook on high heat for 5 minutes",
            "Add a little water if needed and simmer for 5 minutes",
            "Serve with fresh whole wheat rotis"
        ]
    },
    {
        "id": "soya_chunks_rice",
        "name": "Soya Chunks Curry with Rice",
        "meal_type": "dinner",
        "is_veg": True,
        "calories": 400,
        "protein": 28,
        "carbs": 55,
        "fat": 8,
        "cooking_time": "30 mins",
        "portion_size": "1 bowl + 1 cup rice",
        "recipe": [
            "Soak 1 cup soya chunks in hot water for 15 minutes, squeeze dry",
            "Heat oil, add onion paste and cook until brown",
            "Add ginger-garlic paste, tomato puree, and all masalas",
            "Add soya chunks and mix well with the masala",
            "Add water to desired consistency and simmer for 10 minutes",
            "Add kasuri methi and garam masala",
            "Serve hot with steamed rice"
        ]
    },
    {
        "id": "tofu_stir_fry_roti",
        "name": "Tofu Stir Fry with Roti",
        "meal_type": "dinner",
        "is_veg": True,
        "calories": 350,
        "protein": 22,
        "carbs": 38,
        "fat": 14,
        "cooking_time": "20 mins",
        "portion_size": "200g tofu + 2 rotis",
        "recipe": [
            "Press and cube 200g firm tofu",
            "Heat sesame oil in a wok, add garlic and ginger",
            "Add sliced bell peppers, broccoli, and snap peas",
            "Stir fry vegetables on high heat for 3 minutes",
            "Add tofu cubes and toss gently",
            "Add soy sauce, vinegar, and a pinch of sugar",
            "Cook for 3-4 more minutes until tofu is golden",
            "Serve with whole wheat rotis or brown rice"
        ]
    },
    {
        "id": "moong_dal_rice",
        "name": "Moong Dal Fry with Rice",
        "meal_type": "dinner",
        "is_veg": True,
        "calories": 380,
        "protein": 16,
        "carbs": 58,
        "fat": 8,
        "cooking_time": "25 mins",
        "portion_size": "1 bowl dal + 1 cup rice",
        "recipe": [
            "Wash and pressure cook 1 cup yellow moong dal for 3 whistles",
            "Heat ghee, add cumin, garlic, dried red chili",
            "Add chopped onion and tomato, cook until soft",
            "Add turmeric, red chili powder, salt",
            "Add cooked dal and adjust consistency with water",
            "Simmer for 10 minutes",
            "Finish with fresh coriander and lemon juice",
            "Serve with steamed rice"
        ]
    },
    # ===== DINNER - NON-VEG =====
    {
        "id": "tandoori_chicken_salad",
        "name": "Tandoori Chicken with Salad",
        "meal_type": "dinner",
        "is_veg": False,
        "calories": 380,
        "protein": 40,
        "carbs": 12,
        "fat": 18,
        "cooking_time": "35 mins",
        "portion_size": "250g chicken + salad",
        "recipe": [
            "Make cuts in 250g chicken leg pieces",
            "Marinate with curd, tandoori masala, lemon, ginger-garlic paste, oil",
            "Refrigerate for at least 1 hour (overnight for best results)",
            "Bake at 220C for 25-30 minutes or grill until charred",
            "Baste with butter halfway through",
            "Prepare salad: sliced cucumber, onion rings, lemon, chaat masala",
            "Serve chicken hot with fresh salad and mint chutney"
        ]
    },
    {
        "id": "egg_curry_rice",
        "name": "Egg Curry with Rice",
        "meal_type": "dinner",
        "is_veg": False,
        "calories": 420,
        "protein": 24,
        "carbs": 52,
        "fat": 14,
        "cooking_time": "25 mins",
        "portion_size": "3 eggs + 1 cup rice",
        "recipe": [
            "Hard boil 3 eggs, peel and make small cuts",
            "Heat oil, add cumin seeds and bay leaf",
            "Add onion paste and cook until golden",
            "Add ginger-garlic paste, tomato puree, and masalas",
            "Cook until oil separates from masala",
            "Add water and bring to simmer",
            "Gently add eggs and cook for 10 minutes in the gravy",
            "Serve with steamed rice and fresh coriander"
        ]
    },
    {
        "id": "grilled_fish_salad",
        "name": "Grilled Fish with Quinoa Salad",
        "meal_type": "dinner",
        "is_veg": False,
        "calories": 360,
        "protein": 38,
        "carbs": 30,
        "fat": 10,
        "cooking_time": "25 mins",
        "portion_size": "200g fish + salad",
        "recipe": [
            "Marinate 200g fish fillet with lemon, garlic, salt, pepper, dill",
            "Cook 1/2 cup quinoa in salted water as per package instructions",
            "Grill fish on medium-high heat for 4-5 minutes per side",
            "Mix cooled quinoa with diced cucumber, cherry tomatoes, and herbs",
            "Dress salad with olive oil and lemon juice",
            "Plate grilled fish alongside quinoa salad",
            "Garnish with fresh herbs and serve"
        ]
    },
]


def get_foods_by_preference(is_veg, meal_type=None):
    """Get foods filtered by dietary preference and optional meal type."""
    results = []
    for food in FOODS:
        if is_veg and not food["is_veg"]:
            continue
        if meal_type and food["meal_type"] != meal_type:
            continue
        # Non-veg preference gets all foods (veg + non-veg)
        results.append(food)
    return results


def get_food_by_id(food_id):
    """Look up a single food item by its ID."""
    for food in FOODS:
        if food["id"] == food_id:
            return food
    return None
