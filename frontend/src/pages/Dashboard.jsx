import { useState } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Button } from "@/components/ui/button";
import {
  Dumbbell,
  Utensils,
  BrainCircuit,
  ArrowLeft,
  Flame,
  Clock,
  BatteryCharging,
  Target,
  Activity,
} from "lucide-react";
import ModeBadge from "@/components/custom/ModeBadge";
import WorkoutCard from "@/components/custom/WorkoutCard";
import DietCard from "@/components/custom/DietCard";
import ExerciseModal from "@/components/custom/ExerciseModal";
import FoodModal from "@/components/custom/FoodModal";
import MLInsightPanel from "@/components/custom/MLInsightPanel";
import ExplainabilityPanel from "@/components/custom/ExplainabilityPanel";

export default function Dashboard({ data, onBack }) {
  const [selectedExercise, setSelectedExercise] = useState(null);
  const [selectedFood, setSelectedFood] = useState(null);

  const { profile_summary, training_mode, weekly_workout_plan, weekly_diet_plan, ml_insights, explainability, diet_summary } = data;

  const stats = [
    { label: "BMI", value: profile_summary.bmi, sub: profile_summary.bmi_category, icon: Activity },
    { label: "Calories", value: `${profile_summary.target_calories}`, sub: "kcal/day", icon: Flame },
    { label: "Protein", value: `${profile_summary.target_protein}g`, sub: "daily target", icon: Target },
    { label: "Cluster", value: ml_insights.cluster_label, sub: `${(ml_insights.confidence * 100).toFixed(0)}% match`, icon: BrainCircuit },
  ];

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Header */}
      <header className="sticky top-0 z-50 glass-heavy" data-testid="dashboard-header">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Dumbbell className="w-6 h-6 text-[#84cc16]" />
            <h1
              className="text-2xl font-bold tracking-tight uppercase text-slate-900"
              style={{ fontFamily: "Barlow Condensed, sans-serif" }}
            >
              FitCluster <span className="text-[#84cc16]">AI</span>
            </h1>
          </div>
          <div className="flex items-center gap-4">
            <ModeBadge mode={training_mode.mode} label={training_mode.label} />
            <Button
              variant="outline"
              size="sm"
              onClick={onBack}
              className="border-slate-300 text-slate-700 hover:bg-slate-200 transition-all duration-300"
              data-testid="btn-back-to-form"
            >
              <ArrowLeft className="w-4 h-4 mr-1" />
              New Plan
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-6">
        {/* Stats Row */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6" data-testid="stats-row">
          {stats.map((s, i) => (
            <div
              key={s.label}
              className={`glass-surface rounded-xl p-4 animate-fade-in-up stagger-${i + 1}`}
              data-testid={`stat-${s.label.toLowerCase()}`}
            >
              <div className="flex items-center gap-2 mb-2">
                <s.icon className="w-4 h-4 text-[#84cc16]" />
                <span className="text-xs font-bold tracking-widest uppercase text-slate-500">
                  {s.label}
                </span>
              </div>
              <p className="text-xl font-bold text-slate-900" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
                {s.value}
              </p>
              <p className="text-xs text-slate-500 mt-0.5">{s.sub}</p>
            </div>
          ))}
        </div>

        {/* Bento Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {/* Workout Plan - 3 cols */}
          <div className="lg:col-span-3" data-testid="workout-section">
            <div className="glass-surface rounded-xl p-5">
              <div className="flex items-center gap-2 mb-4">
                <Dumbbell className="w-5 h-5 text-[#84cc16]" />
                <h2
                  className="text-xl font-semibold tracking-tight uppercase text-slate-900"
                  style={{ fontFamily: "Barlow Condensed, sans-serif" }}
                >
                  Weekly Workout Plan
                </h2>
              </div>
              <Tabs defaultValue="1" className="w-full">
                <TabsList className="bg-white/85 border border-slate-200 mb-4 flex-wrap h-auto gap-1 p-1">
                  {weekly_workout_plan.map((day) => (
                    <TabsTrigger
                      key={day.day}
                      value={String(day.day)}
                      className="text-xs data-[state=active]:bg-[#84cc16]/10 data-[state=active]:text-[#84cc16] transition-all duration-300"
                      data-testid={`workout-tab-day-${day.day}`}
                    >
                      {day.day_name.substring(0, 3)}
                    </TabsTrigger>
                  ))}
                </TabsList>
                {weekly_workout_plan.map((day) => (
                  <TabsContent key={day.day} value={String(day.day)}>
                    <WorkoutCard day={day} onExerciseClick={setSelectedExercise} />
                  </TabsContent>
                ))}
              </Tabs>
            </div>
          </div>

          {/* Diet Sidebar - 1 col */}
          <div className="lg:col-span-1" data-testid="diet-section">
            <div className="glass-surface rounded-xl p-5">
              <div className="flex items-center gap-2 mb-4">
                <Utensils className="w-5 h-5 text-[#84cc16]" />
                <h2
                  className="text-xl font-semibold tracking-tight uppercase text-slate-900"
                  style={{ fontFamily: "Barlow Condensed, sans-serif" }}
                >
                  Diet Plan
                </h2>
              </div>
              <Tabs defaultValue="1" className="w-full">
                <TabsList className="bg-white/85 border border-slate-200 mb-4 flex-wrap h-auto gap-1 p-1 w-full">
                  {weekly_diet_plan.map((day) => (
                    <TabsTrigger
                      key={day.day}
                      value={String(day.day)}
                      className="text-xs flex-1 data-[state=active]:bg-[#84cc16]/10 data-[state=active]:text-[#84cc16] transition-all duration-300 px-1.5"
                      data-testid={`diet-tab-day-${day.day}`}
                    >
                      {day.day_name.substring(0, 2)}
                    </TabsTrigger>
                  ))}
                </TabsList>
                {weekly_diet_plan.map((day) => (
                  <TabsContent key={day.day} value={String(day.day)}>
                    <DietCard day={day} onFoodClick={setSelectedFood} />
                  </TabsContent>
                ))}
              </Tabs>
            </div>
          </div>

          {/* ML Insights - 2 cols */}
          <div className="lg:col-span-2" data-testid="ml-insights-section">
            <MLInsightPanel insights={ml_insights} />
          </div>

          {/* Explainability - 2 cols */}
          <div className="lg:col-span-2" data-testid="explainability-section">
            <ExplainabilityPanel data={explainability} modeInfo={training_mode} />
          </div>
        </div>
      </main>

      {/* Modals */}
      <ExerciseModal exercise={selectedExercise} onClose={() => setSelectedExercise(null)} />
      <FoodModal food={selectedFood} onClose={() => setSelectedFood(null)} />
    </div>
  );
}
