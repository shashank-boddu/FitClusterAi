import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { PlayCircle, Clock, Info } from "lucide-react";

export default function ExerciseModal({ exercise, onClose }) {
  const videoUrl = exercise
    ? `https://www.youtube.com/embed/${exercise.video_id}?rel=0&modestbranding=1`
    : "";

  return (
    <Dialog open={!!exercise} onOpenChange={(open) => { if (!open) onClose(); }}>
      <DialogContent
        className="bg-slate-100 border-slate-200 max-w-2xl w-[95vw] p-0 overflow-hidden"
        data-testid="exercise-modal"
      >
        {exercise && (
        <>
        {/* Video */}
        <div className="video-container bg-black">
          <iframe
            src={videoUrl}
            title={exercise.name}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            data-testid="exercise-video-iframe"
          />
        </div>

        {/* Details */}
        <div className="p-5">
          <DialogHeader className="mb-4">
            <DialogTitle
              className="text-2xl font-bold tracking-tight uppercase text-slate-900 flex items-center gap-2"
              style={{ fontFamily: "Barlow Condensed, sans-serif" }}
            >
              {exercise.name}
              <span
                className={`text-xs px-2 py-0.5 rounded font-bold tracking-wider ${
                  exercise.role === "primary"
                    ? "bg-[#84cc16]/10 text-[#84cc16]"
                    : "bg-slate-200 text-slate-600"
                }`}
              >
                {exercise.role}
              </span>
            </DialogTitle>
          </DialogHeader>

          <p className="text-sm text-slate-600 mb-4">{exercise.description}</p>

          <div className="grid grid-cols-3 gap-3 mb-4">
            <div className="rounded-lg bg-white/80 p-3 text-center">
              <p className="text-xs text-slate-500 uppercase tracking-wider mb-1">Muscle Group</p>
              <p className="text-sm font-medium text-slate-900">{exercise.muscle_group}</p>
            </div>
            <div className="rounded-lg bg-white/80 p-3 text-center">
              <p className="text-xs text-slate-500 uppercase tracking-wider mb-1">Sets x Reps</p>
              <p className="text-sm font-bold text-[#84cc16]">
                {exercise.sets} x {exercise.reps}
              </p>
            </div>
            <div className="rounded-lg bg-white/80 p-3 text-center">
              <p className="text-xs text-slate-500 uppercase tracking-wider mb-1">Rest</p>
              <div className="flex items-center justify-center gap-1">
                <Clock className="w-3.5 h-3.5 text-slate-600" />
                <p className="text-sm font-medium text-slate-900">{exercise.rest_seconds}s</p>
              </div>
            </div>
          </div>

          {/* XAI Explanation */}
          {exercise.why_chosen && (
            <div className="rounded-lg bg-[#84cc16]/5 border border-[#84cc16]/20 p-3" data-testid="exercise-xai">
              <div className="flex items-center gap-2 mb-1">
                <Info className="w-3.5 h-3.5 text-[#84cc16]" />
                <span className="text-xs font-bold tracking-widest uppercase text-[#84cc16]">
                  Why This Was Chosen
                </span>
              </div>
              <p className="text-xs text-slate-600">{exercise.why_chosen}</p>
            </div>
          )}
        </div>
        </>
        )}
      </DialogContent>
    </Dialog>
  );
}
