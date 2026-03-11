#!/usr/bin/env python3
"""
FitCluster AI - Backend API Testing Suite
Tests all API endpoints for the hybrid intelligent fitness recommendation system.
"""

import requests
import sys
import json
from datetime import datetime

class FitClusterAPITester:
    def __init__(self, base_url="https://fitcluster-ai.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def log_test(self, name, success, details=""):
        """Log test results"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
            print(f"✅ {name} - PASSED")
        else:
            self.failed_tests.append({"name": name, "details": details})
            print(f"❌ {name} - FAILED: {details}")

    def test_health_endpoint(self):
        """Test the health check endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/health", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy" and "FitCluster AI" in data.get("service", ""):
                    self.log_test("Health Check", True)
                    return True
                else:
                    self.log_test("Health Check", False, f"Invalid response data: {data}")
            else:
                self.log_test("Health Check", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_test("Health Check", False, f"Exception: {str(e)}")
        return False

    def test_recommend_endpoint_valid_data(self):
        """Test recommendation endpoint with valid data"""
        valid_payload = {
            "age": 25,
            "gender": "male",
            "height": 175.0,
            "weight": 70.0,
            "fitness_goal": "muscle_gain",
            "experience_level": "intermediate",
            "available_time": "40-50",
            "equipment": "gym",
            "diet_preference": "vegetarian",
            "weekly_adherence": 80,
            "recovery_level": "high"
        }

        try:
            response = requests.post(
                f"{self.base_url}/api/recommend", 
                json=valid_payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                required_fields = [
                    "user_id", "profile_summary", "training_mode", 
                    "weekly_workout_plan", "weekly_diet_plan", 
                    "ml_insights", "explainability"
                ]
                
                missing_fields = [field for field in required_fields if field not in data]
                if not missing_fields:
                    # Check specific nested structure
                    if (data.get("profile_summary", {}).get("bmi") and
                        data.get("training_mode", {}).get("mode") and
                        len(data.get("weekly_workout_plan", [])) == 7 and
                        len(data.get("weekly_diet_plan", [])) == 7 and
                        data.get("ml_insights", {}).get("cluster_id") is not None):
                        
                        self.log_test("Recommend Endpoint - Valid Data", True)
                        self.recommendation_data = data  # Store for detailed validation
                        return True
                    else:
                        self.log_test("Recommend Endpoint - Valid Data", False, "Invalid nested structure")
                else:
                    self.log_test("Recommend Endpoint - Valid Data", False, f"Missing fields: {missing_fields}")
            else:
                self.log_test("Recommend Endpoint - Valid Data", False, f"Status code: {response.status_code}, Response: {response.text}")
        except Exception as e:
            self.log_test("Recommend Endpoint - Valid Data", False, f"Exception: {str(e)}")
        return False

    def test_recommend_endpoint_validation(self):
        """Test recommendation endpoint input validation"""
        invalid_payloads = [
            # Age validation
            {
                "age": 15,  # Below minimum
                "gender": "male",
                "height": 175.0,
                "weight": 70.0,
                "fitness_goal": "muscle_gain",
                "experience_level": "beginner",
                "available_time": "40-50",
                "equipment": "gym",
                "diet_preference": "vegetarian",
                "weekly_adherence": 70,
                "recovery_level": "medium"
            },
            # Invalid gender
            {
                "age": 25,
                "gender": "other",  # Invalid value
                "height": 175.0,
                "weight": 70.0,
                "fitness_goal": "muscle_gain",
                "experience_level": "beginner",
                "available_time": "40-50",
                "equipment": "gym",
                "diet_preference": "vegetarian",
                "weekly_adherence": 70,
                "recovery_level": "medium"
            },
            # Missing required field
            {
                "gender": "male",
                "height": 175.0,
                "weight": 70.0,
                "fitness_goal": "muscle_gain",
                "experience_level": "beginner",
                "available_time": "40-50",
                "equipment": "gym",
                "diet_preference": "vegetarian",
                "weekly_adherence": 70,
                "recovery_level": "medium"
            }
        ]

        validation_passed = 0
        for i, payload in enumerate(invalid_payloads):
            try:
                response = requests.post(
                    f"{self.base_url}/api/recommend", 
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=15
                )
                
                # Should return 422 for validation errors
                if response.status_code == 422:
                    validation_passed += 1
                    print(f"  ✓ Validation test {i+1} passed (422 as expected)")
                else:
                    print(f"  ✗ Validation test {i+1} failed: Expected 422, got {response.status_code}")
            except Exception as e:
                print(f"  ✗ Validation test {i+1} exception: {str(e)}")

        success = validation_passed == len(invalid_payloads)
        self.log_test("Input Validation", success, 
                     f"Passed {validation_passed}/{len(invalid_payloads)} validation tests")
        return success

    def test_workout_plan_structure(self):
        """Test workout plan structure in detail"""
        if not hasattr(self, 'recommendation_data'):
            self.log_test("Workout Plan Structure", False, "No recommendation data available")
            return False

        try:
            workout_plan = self.recommendation_data.get("weekly_workout_plan", [])
            
            # Check 7 days
            if len(workout_plan) != 7:
                self.log_test("Workout Plan Structure", False, f"Expected 7 days, got {len(workout_plan)}")
                return False
            
            # Check each day structure
            for day in workout_plan:
                required_fields = ["day", "day_name", "workout_name", "is_rest_day", "exercises", "explanation"]
                missing_fields = [field for field in required_fields if field not in day]
                if missing_fields:
                    self.log_test("Workout Plan Structure", False, f"Day {day.get('day', '?')} missing: {missing_fields}")
                    return False
                
                # Check exercises structure for non-rest days
                if not day["is_rest_day"]:
                    if not day["exercises"]:
                        self.log_test("Workout Plan Structure", False, f"Day {day['day']} has no exercises but is not rest day")
                        return False
                    
                    for ex in day["exercises"]:
                        ex_required = ["id", "name", "sets", "reps", "video_id", "muscle_group"]
                        ex_missing = [field for field in ex_required if field not in ex]
                        if ex_missing:
                            self.log_test("Workout Plan Structure", False, f"Exercise missing: {ex_missing}")
                            return False
            
            self.log_test("Workout Plan Structure", True)
            return True
            
        except Exception as e:
            self.log_test("Workout Plan Structure", False, f"Exception: {str(e)}")
            return False

    def test_diet_plan_structure(self):
        """Test diet plan structure in detail"""
        if not hasattr(self, 'recommendation_data'):
            self.log_test("Diet Plan Structure", False, "No recommendation data available")
            return False

        try:
            diet_plan = self.recommendation_data.get("weekly_diet_plan", [])
            
            # Check 7 days
            if len(diet_plan) != 7:
                self.log_test("Diet Plan Structure", False, f"Expected 7 days, got {len(diet_plan)}")
                return False
            
            # Check each day structure
            for day in diet_plan:
                required_fields = ["day", "day_name", "meals", "total_calories", "total_protein"]
                missing_fields = [field for field in required_fields if field not in day]
                if missing_fields:
                    self.log_test("Diet Plan Structure", False, f"Diet day {day.get('day', '?')} missing: {missing_fields}")
                    return False
                
                # Check meals structure
                if not day["meals"] or len(day["meals"]) < 3:  # At least 3 meals
                    self.log_test("Diet Plan Structure", False, f"Day {day['day']} has insufficient meals")
                    return False
                
                for meal in day["meals"]:
                    meal_required = ["meal_type", "food"]
                    meal_missing = [field for field in meal_required if field not in meal]
                    if meal_missing:
                        self.log_test("Diet Plan Structure", False, f"Meal missing: {meal_missing}")
                        return False
                    
                    # Check food structure
                    food = meal["food"]
                    food_required = ["id", "name", "calories", "protein", "carbs", "fat"]
                    food_missing = [field for field in food_required if field not in food]
                    if food_missing:
                        self.log_test("Diet Plan Structure", False, f"Food missing: {food_missing}")
                        return False
            
            self.log_test("Diet Plan Structure", True)
            return True
            
        except Exception as e:
            self.log_test("Diet Plan Structure", False, f"Exception: {str(e)}")
            return False

    def test_ml_insights_structure(self):
        """Test ML insights structure"""
        if not hasattr(self, 'recommendation_data'):
            self.log_test("ML Insights Structure", False, "No recommendation data available")
            return False

        try:
            ml_insights = self.recommendation_data.get("ml_insights", {})
            required_fields = [
                "cluster_id", "cluster_label", "confidence", 
                "feature_importance", "similarity_score"
            ]
            
            missing_fields = [field for field in required_fields if field not in ml_insights]
            if missing_fields:
                self.log_test("ML Insights Structure", False, f"Missing fields: {missing_fields}")
                return False
            
            # Check cluster_id is valid (0-5 based on the ML engine)
            cluster_id = ml_insights["cluster_id"]
            if not isinstance(cluster_id, int) or cluster_id < 0 or cluster_id > 5:
                self.log_test("ML Insights Structure", False, f"Invalid cluster_id: {cluster_id}")
                return False
            
            # Check confidence is between 0 and 1
            confidence = ml_insights["confidence"]
            if not isinstance(confidence, (int, float)) or confidence < 0 or confidence > 1:
                self.log_test("ML Insights Structure", False, f"Invalid confidence: {confidence}")
                return False
            
            # Check feature_importance is a dict with expected features
            feature_importance = ml_insights["feature_importance"]
            expected_features = ["Age", "BMI", "Fitness Goal", "Experience", "Adherence", "Recovery", "Equipment", "Time"]
            if not isinstance(feature_importance, dict):
                self.log_test("ML Insights Structure", False, "feature_importance is not a dict")
                return False
            
            missing_features = [f for f in expected_features if f not in feature_importance]
            if missing_features:
                self.log_test("ML Insights Structure", False, f"Missing feature importance: {missing_features}")
                return False
            
            self.log_test("ML Insights Structure", True)
            return True
            
        except Exception as e:
            self.log_test("ML Insights Structure", False, f"Exception: {str(e)}")
            return False

    def test_different_user_profiles(self):
        """Test recommendation with different user profiles"""
        profiles = [
            # Beginner fat loss
            {
                "age": 30, "gender": "female", "height": 165.0, "weight": 75.0,
                "fitness_goal": "fat_loss", "experience_level": "beginner",
                "available_time": "20-30", "equipment": "home",
                "diet_preference": "vegetarian", "weekly_adherence": 60, "recovery_level": "low"
            },
            # Advanced muscle gain
            {
                "age": 28, "gender": "male", "height": 180.0, "weight": 85.0,
                "fitness_goal": "muscle_gain", "experience_level": "advanced",
                "available_time": "60+", "equipment": "gym",
                "diet_preference": "non_vegetarian", "weekly_adherence": 90, "recovery_level": "high"
            },
            # General fitness
            {
                "age": 35, "gender": "female", "height": 160.0, "weight": 60.0,
                "fitness_goal": "general_fitness", "experience_level": "intermediate",
                "available_time": "40-50", "equipment": "gym",
                "diet_preference": "vegetarian", "weekly_adherence": 75, "recovery_level": "medium"
            }
        ]

        successful_profiles = 0
        for i, profile in enumerate(profiles):
            try:
                response = requests.post(
                    f"{self.base_url}/api/recommend", 
                    json=profile,
                    headers={"Content-Type": "application/json"},
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if (data.get("user_id") and 
                        data.get("training_mode", {}).get("mode") and
                        len(data.get("weekly_workout_plan", [])) == 7):
                        successful_profiles += 1
                        print(f"  ✓ Profile {i+1} ({profile['fitness_goal']}) - Success")
                    else:
                        print(f"  ✗ Profile {i+1} - Invalid response structure")
                else:
                    print(f"  ✗ Profile {i+1} - Status: {response.status_code}")
            except Exception as e:
                print(f"  ✗ Profile {i+1} - Exception: {str(e)}")

        success = successful_profiles == len(profiles)
        self.log_test("Different User Profiles", success, 
                     f"Successful: {successful_profiles}/{len(profiles)}")
        return success

    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting FitCluster AI Backend API Tests")
        print(f"Testing endpoint: {self.base_url}")
        print("-" * 60)
        
        # Test health endpoint first
        if not self.test_health_endpoint():
            print("\n❌ Health check failed - stopping tests")
            return False
        
        # Test main functionality
        self.test_recommend_endpoint_valid_data()
        self.test_recommend_endpoint_validation()
        self.test_workout_plan_structure()
        self.test_diet_plan_structure()
        self.test_ml_insights_structure()
        self.test_different_user_profiles()
        
        # Print summary
        print("\n" + "="*60)
        print(f"📊 Test Summary: {self.tests_passed}/{self.tests_run} passed")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"  - {test['name']}: {test['details']}")
        
        success_rate = (self.tests_passed / self.tests_run) * 100 if self.tests_run > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")
        
        return self.tests_passed == self.tests_run

def main():
    tester = FitClusterAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())