"""
FitCluster AI - Hybrid Intelligent Fitness Recommendation System
Main FastAPI server with endpoints for recommendation generation.
Combines rule-based logic with ML-assisted pattern discovery.
"""

from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime, timezone

# Local engine imports
from workout_engine import generate_weekly_workout
from diet_engine import generate_weekly_diet
from ml_engine import run_ml_analysis

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
#mongo_url = os.environ['MONGO_URL']
#client = AsyncIOMotorClient(mongo_url)
#db = client[os.environ['DB_NAME']]

app = FastAPI(title="FitCluster AI", version="1.0.0")
api_router = APIRouter(prefix="/api")

# ──────────────────── MODELS ────────────────────
class UserProfile(BaseModel):
    age: int = Field(ge=16, le=80)
    gender: str = Field(pattern="^(male|female)$")
    height: float = Field(ge=100, le=250)
    weight: float = Field(ge=30, le=200)
    fitness_goal: str = Field(pattern="^(muscle_gain|fat_loss|general_fitness)$")
    experience_level: str = Field(pattern="^(beginner|intermediate|advanced)$")
    available_time: str = Field(pattern="^(20-30|40-50|60\\+)$")
    equipment: str = Field(pattern="^(home|gym)$")
    diet_preference: str = Field(pattern="^(vegetarian|non_vegetarian)$")
    weekly_adherence: int = Field(ge=0, le=100)
    recovery_level: str = Field(pattern="^(low|medium|high)$")


# ──────────────────── ENDPOINTS ────────────────────
@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "FitCluster AI"}


@api_router.post("/recommend")
async def generate_recommendation(profile: UserProfile):
    """
    Main recommendation endpoint.
    1. Runs ML analysis (clustering + similarity)
    2. Generates workout plan (rule-based + ML adjustments)
    3. Generates diet plan (rule-based)
    4. Compiles explainability data
    """
    user_data = profile.model_dump()

    # Calculate BMI
    bmi = round(user_data["weight"] / ((user_data["height"] / 100) ** 2), 1)
    bmi_category = (
        "Underweight" if bmi < 18.5
        else "Normal" if bmi < 25
        else "Overweight" if bmi < 30
        else "Obese"
    )

    # Step 1: ML Analysis
    ml_insights = run_ml_analysis(user_data)

    # Step 2: Generate workout plan with ML adjustments
    workout_result = generate_weekly_workout(user_data, ml_insights["adjustments"])

    # Step 3: Generate diet plan
    diet_result = generate_weekly_diet(user_data)

    # Step 4: Compile rule-based explainability
    rule_explanations = [
        {
            "decision": f"Training Mode: {workout_result['mode_label']}",
            "reason": workout_result["mode_explanation"],
            "type": "rule"
        },
        {
            "decision": f"Calorie Target: {diet_result['target_calories']} kcal/day",
            "reason": diet_result["explanation"],
            "type": "rule"
        },
        {
            "decision": f"Equipment: {user_data['equipment'].title()} workout pool selected",
            "reason": f"Exercise library filtered for {user_data['equipment']} equipment availability",
            "type": "rule"
        },
    ]

    # Step 5: Store user profile in MongoDB for future clustering
    user_record = {
        "id": str(uuid.uuid4()),
        "profile": user_data,
        "bmi": bmi,
        "cluster_id": ml_insights["cluster_id"],
        "cluster_label": ml_insights["cluster_label"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    #await db.user_profiles.insert_one(user_record)

    # Build response (exclude MongoDB _id)
    response = {
        "user_id": user_record["id"],
        "profile_summary": {
            "bmi": bmi,
            "bmi_category": bmi_category,
            "target_calories": diet_result["target_calories"],
            "target_protein": diet_result["macros"]["protein"],
            "target_carbs": diet_result["macros"]["carbs"],
            "target_fat": diet_result["macros"]["fat"],
        },
        "training_mode": {
            "mode": workout_result["mode"],
            "label": workout_result["mode_label"],
            "explanation": workout_result["mode_explanation"],
        },
        "weekly_workout_plan": workout_result["weekly_plan"],
        "weekly_diet_plan": diet_result["weekly_diet"],
        "diet_summary": {
            "bmr": diet_result["bmr"],
            "tdee": diet_result["tdee"],
            "target_calories": diet_result["target_calories"],
            "macros": diet_result["macros"],
        },
        "ml_insights": {
            "cluster_id": ml_insights["cluster_id"],
            "cluster_label": ml_insights["cluster_label"],
            "cluster_description": ml_insights["cluster_description"],
            "cluster_recommendation": ml_insights["cluster_recommendation"],
            "confidence": ml_insights["confidence"],
            "feature_importance": ml_insights["feature_importance"],
            "similarity_score": ml_insights["similarity"]["average_similarity"],
            "similar_profiles_count": len(ml_insights["similarity"]["top_similar_indices"]),
        },
        "explainability": {
            "rule_based_decisions": rule_explanations,
            "ml_assisted_insights": ml_insights["ml_explanations"],
        },
    }

    return response


# Include router & middleware
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


#@app.on_event("shutdown")
#async def shutdown_db_client():
#    client.close()
