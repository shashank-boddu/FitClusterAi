# FitCluster AI - PRD

## Problem Statement
Build a hybrid intelligent fitness recommendation system combining rule-based logic with ML (K-Means clustering, cosine similarity) for a BTech final-year project. No paid APIs.

## Architecture
- **Frontend**: React + Tailwind + Shadcn UI + Framer Motion + Recharts
- **Backend**: FastAPI + scikit-learn + MongoDB (Motor)
- **ML**: K-Means (6 clusters) + Cosine Similarity + Feature Importance

## User Personas
- BTech students presenting academic project
- Fitness beginners/intermediates seeking personalized plans

## Core Requirements
- Multi-step input form (11 parameters)
- Rule-based workout engine (3 modes: Performance/Balanced/Recovery)
- Indian diet plan generator (Veg/Non-Veg, macros, recipes)
- ML clustering for user profiling (6 fitness personas)
- Explainable AI (XAI) for every decision
- YouTube exercise video embeds (deterministic mapping)

## What's Been Implemented (Feb 2026)
- [x] 4-step wizard form with animated transitions
- [x] Rule-based workout engine (50+ exercises, Home/Gym pools)
- [x] Diet engine with 35+ Indian food items + 13 supplements, full recipes
- [x] Calorie-matched meal plans (supplements auto-added to meet BMR/TDEE targets)
- [x] K-Means clustering (6 personas) + cosine similarity
- [x] Feature importance radar chart
- [x] Exercise video modals (YouTube embeds)
- [x] Food detail modals (macros + step-by-step recipes)
- [x] Explainability panel (rule-based + ML decisions)
- [x] Dark theme with neon lime accents
- [x] Mode badge (Performance/Balanced/Recovery)
- [x] BMR/TDEE/Macro calculation
- [x] MongoDB storage for user profiles

## Prioritized Backlog
- P1: Export plan as PDF for offline use
- P1: User history/comparison across sessions
- P2: Progressive overload tracking
- P2: More exercise video variety
- P3: Admin dashboard with clustering analytics
