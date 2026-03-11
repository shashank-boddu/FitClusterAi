import { PlayCircle, Clock, Info } from "lucide-react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

export default function WorkoutCard({ day, onExerciseClick }) {
  if (day.is_rest_day) {
    return (
      <div
        className="rounded-lg border border-slate-200 bg-white/70 p-6 text-center"
        data-testid={`workout-day-${day.day}-rest`}
      >
        <p className="text-lg font-semibold text-slate-600" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
          {day.workout_name}
        </p>
        <p className="text-sm text-slate-500 mt-2">{day.explanation}</p>
      </div>
    );
  }

  return (
    <div data-testid={`workout-day-${day.day}`}>
      <div className="flex items-center justify-between mb-3">
        <h3
          className="text-lg font-semibold text-slate-900 uppercase tracking-wide"
          style={{ fontFamily: "Barlow Condensed, sans-serif" }}
        >
          {day.workout_name}
        </h3>
        <span className="text-xs text-slate-500">{day.exercises.length} exercises</span>
      </div>
      <p className="text-xs text-slate-500 mb-4">{day.explanation}</p>

      <div className="space-y-2">
        {day.exercises.map((ex, idx) => (
          <button
            key={`${ex.id}-${idx}`}
            onClick={() => onExerciseClick(ex)}
            className="w-full flex items-center gap-4 p-3 rounded-lg border border-slate-200 bg-white/75 hover:border-[#84cc16]/30 hover:bg-[#84cc16]/5 transition-all duration-300 text-left group"
            data-testid={`exercise-${ex.id}`}
          >
            {/* Play icon */}
            <div className="flex-shrink-0 w-10 h-10 rounded-lg bg-slate-200 flex items-center justify-center group-hover:bg-[#84cc16]/10 transition-all duration-300">
              <PlayCircle className="w-5 h-5 text-slate-500 group-hover:text-[#84cc16] transition-all duration-300" />
            </div>

            {/* Details */}
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className="text-sm font-medium text-slate-900 truncate">{ex.name}</span>
                <span
                  className={`text-[10px] px-1.5 py-0.5 rounded uppercase font-bold tracking-wider ${
                    ex.role === "primary"
                      ? "bg-[#84cc16]/10 text-[#84cc16]"
                      : "bg-slate-200 text-slate-600"
                  }`}
                >
                  {ex.role}
                </span>
              </div>
              <div className="flex items-center gap-3 mt-1">
                <span className="text-xs text-slate-500">{ex.muscle_group}</span>
              </div>
            </div>

            {/* Sets x Reps */}
            <div className="flex-shrink-0 text-right">
              <p className="text-sm font-bold text-slate-900" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
                {ex.sets} x {ex.reps}
              </p>
              <div className="flex items-center gap-1 text-xs text-slate-500 justify-end">
                <Clock className="w-3 h-3" />
                {ex.rest_seconds}s rest
              </div>
            </div>

            {/* XAI Tooltip */}
            {ex.why_chosen && (
              <TooltipProvider delayDuration={200}>
                <Tooltip>
                  <TooltipTrigger asChild>
                    <div className="flex-shrink-0">
                      <Info className="w-4 h-4 text-slate-500 hover:text-[#84cc16] transition-colors" />
                    </div>
                  </TooltipTrigger>
                  <TooltipContent className="bg-white border-slate-300 text-slate-700 max-w-xs text-xs">
                    {ex.why_chosen}
                  </TooltipContent>
                </Tooltip>
              </TooltipProvider>
            )}
          </button>
        ))}
      </div>
    </div>
  );
}
