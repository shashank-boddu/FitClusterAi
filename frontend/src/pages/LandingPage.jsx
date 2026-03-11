import { useState } from "react";
import axios from "axios";
import { toast } from "sonner";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Slider } from "@/components/ui/slider";
import { Progress } from "@/components/ui/progress";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Dumbbell,
  ArrowRight,
  ArrowLeft,
  Flame,
  Loader2,
} from "lucide-react";

const API = "http://localhost:5000/api";


const STEPS = [
  { id: 0, title: "BODY METRICS", subtitle: "Age, Gender, Height, Weight" },
  { id: 1, title: "FITNESS PROFILE", subtitle: "Goal & Experience Level" },
  { id: 2, title: "TRAINING SETUP", subtitle: "Time & Equipment" },
  { id: 3, title: "LIFESTYLE", subtitle: "Diet, Adherence & Recovery" },
];

const INITIAL_FORM = {
  age: "",
  gender: "male",
  height: "",
  weight: "",
  fitness_goal: "muscle_gain",
  experience_level: "beginner",
  available_time: "40-50",
  equipment: "gym",
  diet_preference: "vegetarian",
  weekly_adherence: 70,
  recovery_level: "medium",
};

export default function LandingPage({ onResult }) {
  const [step, setStep] = useState(0);
  const [form, setForm] = useState(INITIAL_FORM);
  const [loading, setLoading] = useState(false);

  const update = (key, value) => setForm((p) => ({ ...p, [key]: value }));
  const progress = ((step + 1) / STEPS.length) * 100;

  const canNext = () => {
    if (step === 0) return form.age && form.height && form.weight;
    return true;
  };

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const payload = {
        ...form,
        age: parseInt(form.age),
        height: parseFloat(form.height),
        weight: parseFloat(form.weight),
      };
      const { data } = await axios.post(`${API}/recommend`, payload);
      onResult(data);
      toast.success("Recommendation generated successfully!");
    } catch (err) {
      const msg = err.response?.data?.detail;
      toast.error(
        typeof msg === "string" ? msg : "Failed to generate recommendation"
      );
    } finally {
      setLoading(false);
    }
  };

  const slideVariants = {
    enter: (d) => ({ x: d > 0 ? 200 : -200, opacity: 0 }),
    center: { x: 0, opacity: 1 },
    exit: (d) => ({ x: d < 0 ? 200 : -200, opacity: 0 }),
  };

  const [direction, setDirection] = useState(1);
  const goNext = () => {
    if (!canNext()) {
      toast.error("Please fill in all required fields");
      return;
    }
    setDirection(1);
    setStep((s) => Math.min(s + 1, 3));
  };
  const goBack = () => {
    setDirection(-1);
    setStep((s) => Math.max(s - 1, 0));
  };

  return (
    <div
      className="relative min-h-screen flex items-center justify-center p-4"
      style={{
        backgroundImage:
          "radial-gradient(circle at 12% 10%, rgba(132,204,22,0.16), transparent 36%), radial-gradient(circle at 88% 4%, rgba(16,185,129,0.1), transparent 28%), linear-gradient(180deg, #f7fbea 0%, #eef8d2 100%)",
      }}
    >
      {/* Top glow */}
      <div className="absolute top-0 left-0 right-0 h-48 glow-top pointer-events-none" />

      <div className="w-full max-w-xl relative z-10">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 mb-4">
            <Dumbbell className="w-8 h-8 text-[#84cc16]" />
            <h1
              data-testid="app-title"
              className="text-5xl font-bold tracking-tight uppercase"
              style={{ fontFamily: "Barlow Condensed, sans-serif" }}
            >
              FitCluster <span className="text-[#84cc16]">AI</span>
            </h1>
          </div>
          <p className="text-sm text-slate-600 tracking-wide uppercase">
            Hybrid Intelligent Fitness Recommendation System
          </p>
        </div>

        {/* Progress */}
        <div className="mb-6">
          <div className="flex justify-between mb-2">
            {STEPS.map((s, i) => (
              <button
                key={s.id}
                onClick={() => {
                  setDirection(i > step ? 1 : -1);
                  setStep(i);
                }}
                className={`text-xs font-bold tracking-widest uppercase transition-all duration-300 ${
                  i <= step ? "text-[#84cc16]" : "text-slate-500"
                }`}
                data-testid={`step-indicator-${i}`}
              >
                {i + 1}
              </button>
            ))}
          </div>
          <Progress value={progress} className="h-1.5 bg-slate-200" data-testid="form-progress" />
        </div>

        {/* Form Card */}
        <div className="glass-heavy rounded-xl p-8" data-testid="form-card">
          <div className="mb-6">
            <h2
              className="text-2xl font-semibold tracking-tight uppercase text-slate-900"
              style={{ fontFamily: "Barlow Condensed, sans-serif" }}
            >
              {STEPS[step].title}
            </h2>
            <p className="text-sm text-slate-600 mt-1">{STEPS[step].subtitle}</p>
          </div>

          <AnimatePresence mode="wait" custom={direction}>
            <motion.div
              key={step}
              custom={direction}
              variants={slideVariants}
              initial="enter"
              animate="center"
              exit="exit"
              transition={{ duration: 0.25, ease: "easeInOut" }}
            >
              {step === 0 && (
                <div className="space-y-5" data-testid="step-body-metrics">
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-2 block">
                        Age
                      </Label>
                      <Input
                        data-testid="input-age"
                        type="number"
                        placeholder="e.g. 25"
                        className="h-12 bg-white/80 border-slate-300 text-slate-900 placeholder:text-slate-500"
                        value={form.age}
                        onChange={(e) => update("age", e.target.value)}
                        min={16}
                        max={80}
                      />
                    </div>
                    <div>
                      <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-2 block">
                        Gender
                      </Label>
                      <Select value={form.gender} onValueChange={(v) => update("gender", v)}>
                        <SelectTrigger
                          data-testid="select-gender"
                          className="h-12 bg-white/80 border-slate-300 text-slate-900"
                        >
                          <SelectValue />
                        </SelectTrigger>
                        <SelectContent className="bg-white border-slate-300">
                          <SelectItem value="male">Male</SelectItem>
                          <SelectItem value="female">Female</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-2 block">
                        Height (cm)
                      </Label>
                      <Input
                        data-testid="input-height"
                        type="number"
                        placeholder="e.g. 175"
                        className="h-12 bg-white/80 border-slate-300 text-slate-900 placeholder:text-slate-500"
                        value={form.height}
                        onChange={(e) => update("height", e.target.value)}
                        min={100}
                        max={250}
                      />
                    </div>
                    <div>
                      <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-2 block">
                        Weight (kg)
                      </Label>
                      <Input
                        data-testid="input-weight"
                        type="number"
                        placeholder="e.g. 70"
                        className="h-12 bg-white/80 border-slate-300 text-slate-900 placeholder:text-slate-500"
                        value={form.weight}
                        onChange={(e) => update("weight", e.target.value)}
                        min={30}
                        max={200}
                      />
                    </div>
                  </div>
                </div>
              )}

              {step === 1 && (
                <div className="space-y-6" data-testid="step-fitness-profile">
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-3 block">
                      Fitness Goal
                    </Label>
                    <RadioGroup
                      value={form.fitness_goal}
                      onValueChange={(v) => update("fitness_goal", v)}
                      className="grid grid-cols-1 gap-3"
                    >
                      {[
                        { value: "muscle_gain", label: "Muscle Gain", desc: "Build strength & size" },
                        { value: "fat_loss", label: "Fat Loss", desc: "Reduce body fat" },
                        { value: "general_fitness", label: "General Fitness", desc: "Overall health" },
                      ].map((opt) => (
                        <label
                          key={opt.value}
                          className={`flex items-center gap-3 p-4 rounded-lg border cursor-pointer transition-all duration-300 ${
                            form.fitness_goal === opt.value
                              ? "border-[#84cc16]/50 bg-[#84cc16]/5"
                              : "border-slate-300/70 bg-white/70 hover:border-slate-400"
                          }`}
                          data-testid={`goal-${opt.value}`}
                        >
                          <RadioGroupItem value={opt.value} className="border-slate-400 text-[#84cc16]" />
                          <div>
                            <span className="font-medium text-slate-900">{opt.label}</span>
                            <span className="text-xs text-slate-500 ml-2">{opt.desc}</span>
                          </div>
                        </label>
                      ))}
                    </RadioGroup>
                  </div>
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-3 block">
                      Experience Level
                    </Label>
                    <RadioGroup
                      value={form.experience_level}
                      onValueChange={(v) => update("experience_level", v)}
                      className="grid grid-cols-3 gap-3"
                    >
                      {["beginner", "intermediate", "advanced"].map((lvl) => (
                        <label
                          key={lvl}
                          className={`text-center p-3 rounded-lg border cursor-pointer transition-all duration-300 ${
                            form.experience_level === lvl
                              ? "border-[#84cc16]/50 bg-[#84cc16]/5"
                              : "border-slate-300/70 bg-white/70 hover:border-slate-400"
                          }`}
                          data-testid={`exp-${lvl}`}
                        >
                          <RadioGroupItem value={lvl} className="sr-only" />
                          <span className="text-sm font-medium capitalize text-slate-900">{lvl}</span>
                        </label>
                      ))}
                    </RadioGroup>
                  </div>
                </div>
              )}

              {step === 2 && (
                <div className="space-y-6" data-testid="step-training-setup">
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-3 block">
                      Available Time Per Workout
                    </Label>
                    <RadioGroup
                      value={form.available_time}
                      onValueChange={(v) => update("available_time", v)}
                      className="grid grid-cols-3 gap-3"
                    >
                      {[
                        { value: "20-30", label: "20-30 min" },
                        { value: "40-50", label: "40-50 min" },
                        { value: "60+", label: "60+ min" },
                      ].map((opt) => (
                        <label
                          key={opt.value}
                          className={`text-center p-4 rounded-lg border cursor-pointer transition-all duration-300 ${
                            form.available_time === opt.value
                              ? "border-[#84cc16]/50 bg-[#84cc16]/5"
                              : "border-slate-300/70 bg-white/70 hover:border-slate-400"
                          }`}
                          data-testid={`time-${opt.value}`}
                        >
                          <RadioGroupItem value={opt.value} className="sr-only" />
                          <span className="text-sm font-medium text-slate-900">{opt.label}</span>
                        </label>
                      ))}
                    </RadioGroup>
                  </div>
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-3 block">
                      Equipment Available
                    </Label>
                    <RadioGroup
                      value={form.equipment}
                      onValueChange={(v) => update("equipment", v)}
                      className="grid grid-cols-2 gap-3"
                    >
                      {[
                        { value: "home", label: "Home", desc: "Bodyweight & bands" },
                        { value: "gym", label: "Gym", desc: "Full equipment access" },
                      ].map((opt) => (
                        <label
                          key={opt.value}
                          className={`text-center p-4 rounded-lg border cursor-pointer transition-all duration-300 ${
                            form.equipment === opt.value
                              ? "border-[#84cc16]/50 bg-[#84cc16]/5"
                              : "border-slate-300/70 bg-white/70 hover:border-slate-400"
                          }`}
                          data-testid={`equip-${opt.value}`}
                        >
                          <RadioGroupItem value={opt.value} className="sr-only" />
                          <span className="text-sm font-semibold text-slate-900">{opt.label}</span>
                          <span className="block text-xs text-slate-500 mt-1">{opt.desc}</span>
                        </label>
                      ))}
                    </RadioGroup>
                  </div>
                </div>
              )}

              {step === 3 && (
                <div className="space-y-6" data-testid="step-lifestyle">
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-3 block">
                      Diet Preference
                    </Label>
                    <RadioGroup
                      value={form.diet_preference}
                      onValueChange={(v) => update("diet_preference", v)}
                      className="grid grid-cols-2 gap-3"
                    >
                      {[
                        { value: "vegetarian", label: "Vegetarian" },
                        { value: "non_vegetarian", label: "Non-Vegetarian" },
                      ].map((opt) => (
                        <label
                          key={opt.value}
                          className={`text-center p-4 rounded-lg border cursor-pointer transition-all duration-300 ${
                            form.diet_preference === opt.value
                              ? "border-[#84cc16]/50 bg-[#84cc16]/5"
                              : "border-slate-300/70 bg-white/70 hover:border-slate-400"
                          }`}
                          data-testid={`diet-${opt.value}`}
                        >
                          <RadioGroupItem value={opt.value} className="sr-only" />
                          <span className="text-sm font-medium text-slate-900">{opt.label}</span>
                        </label>
                      ))}
                    </RadioGroup>
                  </div>
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-2 block">
                      Weekly Adherence: <span className="text-[#84cc16]">{form.weekly_adherence}%</span>
                    </Label>
                    <Slider
                      data-testid="slider-adherence"
                      value={[form.weekly_adherence]}
                      onValueChange={(v) => update("weekly_adherence", v[0])}
                      min={0}
                      max={100}
                      step={5}
                      className="mt-3"
                    />
                    <div className="flex justify-between text-xs text-slate-500 mt-1">
                      <span>Low</span>
                      <span>High</span>
                    </div>
                  </div>
                  <div>
                    <Label className="text-xs font-bold tracking-widest uppercase text-slate-600 mb-3 block">
                      Recovery Level
                    </Label>
                    <RadioGroup
                      value={form.recovery_level}
                      onValueChange={(v) => update("recovery_level", v)}
                      className="grid grid-cols-3 gap-3"
                    >
                      {["low", "medium", "high"].map((lvl) => (
                        <label
                          key={lvl}
                          className={`text-center p-3 rounded-lg border cursor-pointer transition-all duration-300 ${
                            form.recovery_level === lvl
                              ? "border-[#84cc16]/50 bg-[#84cc16]/5"
                              : "border-slate-300/70 bg-white/70 hover:border-slate-400"
                          }`}
                          data-testid={`recovery-${lvl}`}
                        >
                          <RadioGroupItem value={lvl} className="sr-only" />
                          <span className="text-sm font-medium capitalize text-slate-900">{lvl}</span>
                        </label>
                      ))}
                    </RadioGroup>
                  </div>
                </div>
              )}
            </motion.div>
          </AnimatePresence>

          {/* Navigation */}
          <div className="flex justify-between mt-8">
            <Button
              variant="outline"
              onClick={goBack}
              disabled={step === 0}
              className="border-slate-300 text-slate-700 hover:bg-slate-200 transition-all duration-300"
              data-testid="btn-back"
            >
              <ArrowLeft className="w-4 h-4 mr-2" />
              Back
            </Button>

            {step < 3 ? (
              <Button
                onClick={goNext}
                className="bg-[#84cc16] text-black hover:bg-[#65a30d] font-semibold transition-all duration-300"
                data-testid="btn-next"
              >
                Next
                <ArrowRight className="w-4 h-4 ml-2" />
              </Button>
            ) : (
              <Button
                onClick={handleSubmit}
                disabled={loading}
                className="bg-[#84cc16] text-black hover:bg-[#65a30d] font-semibold px-8 transition-all duration-300 neon-glow"
                data-testid="btn-generate"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Flame className="w-4 h-4 mr-2" />
                    Generate Plan
                  </>
                )}
              </Button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
