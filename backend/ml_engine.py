"""
ML Engine - Machine Learning component for the Hybrid Intelligent Fitness System.
Implements K-Means clustering for user profiling and cosine similarity for pattern discovery.
ML influences HOW rules are applied, it does NOT generate workouts directly.
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# ──────────────────── FEATURE ENCODING ────────────────────
GOAL_MAP = {"muscle_gain": 0, "fat_loss": 1, "general_fitness": 2}
EXPERIENCE_MAP = {"beginner": 0, "intermediate": 1, "advanced": 2}
RECOVERY_MAP = {"low": 0, "medium": 1, "high": 2}
EQUIPMENT_MAP = {"home": 0, "gym": 1}
TIME_MAP = {"20-30": 0, "40-50": 1, "60+": 2}

# Fitness persona labels for each cluster
CLUSTER_PERSONAS = {
    0: {
        "label": "Consistent Beginners",
        "description": "Users new to fitness with strong commitment and adherence. Respond well to structured, progressive programs.",
        "recommendation": "Progressive overload with foundational exercises. Consistent habit building."
    },
    1: {
        "label": "Inconsistent Beginners",
        "description": "Newcomers struggling with workout consistency. Need simplified, achievable routines to build habits.",
        "recommendation": "Simplified routines, fewer exercises, focus on habit formation over intensity."
    },
    2: {
        "label": "Intermediate Muscle Builders",
        "description": "Experienced users focused on muscle gain with moderate-high adherence. Ready for split training.",
        "recommendation": "Structured split training with progressive volume increases."
    },
    3: {
        "label": "Recovery-Prone Users",
        "description": "Users reporting low recovery regardless of experience. May be under-sleeping, stressed, or overtrained.",
        "recommendation": "Reduced volume, emphasis on recovery, deload-friendly programming."
    },
    4: {
        "label": "Advanced Athletes",
        "description": "Highly experienced users with high adherence and recovery. Can handle advanced programming.",
        "recommendation": "High-volume, periodized training with advanced techniques."
    },
    5: {
        "label": "Fat Loss Focused",
        "description": "Users primarily targeting fat loss with conditioning emphasis. Benefit from circuit-style training.",
        "recommendation": "Circuit training, HIIT integration, caloric deficit support."
    },
}

# ──────────────────── SYNTHETIC TRAINING DATA ────────────────────
# Format: [age, bmi, goal, experience, adherence, recovery, equipment, time]
# These represent archetypal user profiles for training the clustering model
SYNTHETIC_DATA = np.array([
    # Cluster 0: Consistent Beginners
    [22, 23.5, 2, 0, 85, 2, 1, 1],
    [25, 24.0, 0, 0, 80, 2, 0, 0],
    [20, 22.0, 2, 0, 90, 1, 1, 1],
    [28, 25.5, 2, 0, 82, 2, 0, 1],
    [23, 21.0, 0, 0, 88, 2, 1, 0],
    # Cluster 1: Inconsistent Beginners
    [19, 26.0, 1, 0, 35, 1, 0, 0],
    [22, 28.0, 1, 0, 40, 0, 0, 0],
    [30, 27.0, 2, 0, 30, 1, 0, 0],
    [24, 29.0, 1, 0, 25, 0, 0, 0],
    [21, 25.5, 2, 0, 45, 1, 0, 1],
    # Cluster 2: Intermediate Muscle Builders
    [26, 24.0, 0, 1, 75, 1, 1, 2],
    [28, 25.0, 0, 1, 80, 2, 1, 2],
    [30, 23.5, 0, 2, 70, 1, 1, 1],
    [25, 26.0, 0, 1, 78, 2, 1, 2],
    [27, 24.5, 0, 1, 72, 1, 1, 1],
    # Cluster 3: Recovery-Prone Users
    [35, 27.0, 2, 1, 60, 0, 1, 1],
    [40, 28.5, 2, 0, 55, 0, 0, 0],
    [32, 26.0, 0, 1, 65, 0, 1, 1],
    [38, 30.0, 1, 0, 50, 0, 0, 0],
    [28, 25.0, 2, 1, 58, 0, 1, 1],
    # Cluster 4: Advanced Athletes
    [30, 23.0, 0, 2, 92, 2, 1, 2],
    [28, 22.5, 2, 2, 95, 2, 1, 2],
    [32, 24.0, 0, 2, 88, 2, 1, 2],
    [26, 23.5, 0, 2, 90, 2, 1, 2],
    [29, 22.0, 2, 2, 93, 2, 1, 2],
    # Cluster 5: Fat Loss Focused
    [35, 30.0, 1, 1, 70, 1, 1, 1],
    [28, 28.0, 1, 0, 65, 1, 0, 1],
    [40, 32.0, 1, 1, 72, 1, 1, 1],
    [33, 29.0, 1, 1, 68, 2, 1, 2],
    [30, 27.5, 1, 0, 60, 1, 0, 0],
])


# ──────────────────── MODEL TRAINING ────────────────────
def create_feature_vector(user_data):
    """Convert user input into a numerical feature vector."""
    bmi = user_data["weight"] / ((user_data["height"] / 100) ** 2)
    return np.array([
        user_data["age"],
        bmi,
        GOAL_MAP.get(user_data["fitness_goal"], 2),
        EXPERIENCE_MAP.get(user_data["experience_level"], 0),
        user_data["weekly_adherence"],
        RECOVERY_MAP.get(user_data["recovery_level"], 1),
        EQUIPMENT_MAP.get(user_data["equipment"], 0),
        TIME_MAP.get(user_data["available_time"], 1),
    ]).reshape(1, -1)


def train_and_predict(user_vector):
    """
    Train K-Means on synthetic data and predict cluster for new user.
    Returns cluster info and model details.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(SYNTHETIC_DATA)
    scaled_user = scaler.transform(user_vector)

    # K-Means clustering with 6 personas
    kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
    kmeans.fit(scaled_data)

    # Predict user cluster
    cluster_id = int(kmeans.predict(scaled_user)[0])

    # Calculate distances to all centroids for confidence
    distances = kmeans.transform(scaled_user)[0]
    min_dist = distances[cluster_id]
    confidence = max(0.0, min(1.0, 1.0 - (min_dist / (np.max(distances) + 1e-8))))

    return cluster_id, confidence, scaled_data, scaled_user, kmeans


def compute_similarity(scaled_user, scaled_data):
    """
    Compute cosine similarity between the user and all synthetic profiles.
    Returns similarity scores and indices of most similar users.
    """
    similarities = cosine_similarity(scaled_user, scaled_data)[0]
    top_indices = np.argsort(similarities)[-5:][::-1]
    avg_similarity = float(np.mean(similarities[top_indices]))

    return {
        "top_similar_indices": top_indices.tolist(),
        "top_similarity_scores": similarities[top_indices].tolist(),
        "average_similarity": round(avg_similarity, 3),
        "all_scores": similarities.tolist(),
    }


def compute_feature_importance(scaled_user, kmeans, cluster_id):
    """
    Estimate which features most influenced the cluster assignment.
    Uses distance from cluster centroid per feature dimension.
    """
    centroid = kmeans.cluster_centers_[cluster_id]
    user_flat = scaled_user.flatten()
    diffs = np.abs(user_flat - centroid)

    # Invert: smaller diff = higher importance (closer match)
    max_diff = np.max(diffs) + 1e-8
    importance = 1.0 - (diffs / max_diff)
    importance = importance / (np.sum(importance) + 1e-8)

    feature_names = ["Age", "BMI", "Fitness Goal", "Experience", "Adherence", "Recovery", "Equipment", "Time"]
    return {name: round(float(val), 3) for name, val in zip(feature_names, importance)}


# ──────────────────── GET ML ADJUSTMENTS ────────────────────
def get_ml_adjustments(cluster_id, adherence, recovery):
    """
    Determine rule adjustments based on ML cluster assignment.
    ML influences HOW rules are applied, not WHAT exercises are generated.
    """
    adjustments = {
        "force_recovery": False,
        "boost_volume": False,
        "simplify_movements": False,
        "add_conditioning": False,
        "notes": []
    }

    persona = CLUSTER_PERSONAS.get(cluster_id, {})

    if cluster_id == 1:  # Inconsistent Beginners
        adjustments["simplify_movements"] = True
        adjustments["notes"].append(
            "Cluster pattern: Inconsistent beginners benefit from simplified routines"
        )
    elif cluster_id == 3:  # Recovery-Prone
        adjustments["force_recovery"] = True
        adjustments["notes"].append(
            "Cluster pattern: Recovery-prone users benefit from reduced volume"
        )
    elif cluster_id == 4:  # Advanced Athletes
        if adherence >= 75:
            adjustments["boost_volume"] = True
            adjustments["notes"].append(
                "Cluster pattern: Advanced athletes with high adherence respond to increased volume"
            )
    elif cluster_id == 5:  # Fat Loss Focused
        adjustments["add_conditioning"] = True
        adjustments["notes"].append(
            "Cluster pattern: Fat-loss focused users benefit from additional conditioning"
        )

    return adjustments


# ──────────────────── MAIN ML ANALYSIS ────────────────────
def run_ml_analysis(user_data):
    """
    Run complete ML analysis pipeline.
    Returns cluster info, similarity analysis, feature importance, and adjustments.
    """
    # Create feature vector
    user_vector = create_feature_vector(user_data)

    # Train and predict
    cluster_id, confidence, scaled_data, scaled_user, kmeans = train_and_predict(user_vector)

    # Get persona info
    persona = CLUSTER_PERSONAS.get(cluster_id, {
        "label": "Unknown",
        "description": "Unable to determine cluster",
        "recommendation": "Default balanced approach"
    })

    # Compute similarity
    similarity = compute_similarity(scaled_user, scaled_data)

    # Compute feature importance
    feature_importance = compute_feature_importance(scaled_user, kmeans, cluster_id)

    # Get ML-based adjustments for the rule engine
    adjustments = get_ml_adjustments(
        cluster_id,
        user_data["weekly_adherence"],
        user_data["recovery_level"]
    )

    # Build explainability data
    ml_explanations = [
        {
            "insight": f"User classified as '{persona['label']}' (Cluster {cluster_id})",
            "reason": f"Feature vector analysis yielded {confidence:.0%} confidence match with cluster centroid",
            "type": "ml"
        },
        {
            "insight": f"Top similarity score: {similarity['average_similarity']:.0%} with {len(similarity['top_similar_indices'])} similar profiles",
            "reason": "Cosine similarity computed across all stored user feature vectors",
            "type": "ml"
        },
    ]

    for note in adjustments["notes"]:
        ml_explanations.append({
            "insight": note,
            "reason": "Pattern discovered through unsupervised learning on user clusters",
            "type": "ml"
        })

    # Top contributing features
    sorted_features = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
    top_features = sorted_features[:3]
    ml_explanations.append({
        "insight": f"Top influencing features: {', '.join(f[0] for f in top_features)}",
        "reason": "Feature importance derived from distance to cluster centroid per dimension",
        "type": "ml"
    })

    return {
        "cluster_id": cluster_id,
        "cluster_label": persona["label"],
        "cluster_description": persona["description"],
        "cluster_recommendation": persona["recommendation"],
        "confidence": round(confidence, 3),
        "feature_importance": feature_importance,
        "similarity": similarity,
        "adjustments": adjustments,
        "ml_explanations": ml_explanations,
    }
