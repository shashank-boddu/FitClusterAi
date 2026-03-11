import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Flame, Clock, ChefHat } from "lucide-react";

export default function FoodModal({ food, onClose }) {
  return (
    <Dialog open={!!food} onOpenChange={(open) => { if (!open) onClose(); }}>
      <DialogContent
        className="bg-slate-100 border-slate-200 max-w-lg w-[95vw]"
        data-testid="food-modal"
      >
        {food && (
        <>
        <DialogHeader>
          <DialogTitle
            className="text-2xl font-bold tracking-tight uppercase text-slate-900"
            style={{ fontFamily: "Barlow Condensed, sans-serif" }}
          >
            {food.name}
          </DialogTitle>
        </DialogHeader>

        {/* Macros Grid */}
        <div className="grid grid-cols-4 gap-2 my-4" data-testid="food-macros">
          <div className="rounded-lg bg-white/80 p-3 text-center">
            <Flame className="w-4 h-4 text-orange-400 mx-auto mb-1" />
            <p className="text-lg font-bold text-slate-900" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
              {food.calories}
            </p>
            <p className="text-[10px] text-slate-500 uppercase tracking-wider">Calories</p>
          </div>
          <div className="rounded-lg bg-white/80 p-3 text-center">
            <p className="text-lg font-bold text-[#84cc16]" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
              {food.protein}g
            </p>
            <p className="text-[10px] text-slate-500 uppercase tracking-wider">Protein</p>
          </div>
          <div className="rounded-lg bg-white/80 p-3 text-center">
            <p className="text-lg font-bold text-cyan-400" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
              {food.carbs}g
            </p>
            <p className="text-[10px] text-slate-500 uppercase tracking-wider">Carbs</p>
          </div>
          <div className="rounded-lg bg-white/80 p-3 text-center">
            <p className="text-lg font-bold text-amber-400" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
              {food.fat}g
            </p>
            <p className="text-[10px] text-slate-500 uppercase tracking-wider">Fat</p>
          </div>
        </div>

        {/* Portion & Cooking Time */}
        <div className="flex gap-4 mb-4">
          <div className="flex items-center gap-2 text-sm text-slate-600">
            <Clock className="w-4 h-4 text-slate-500" />
            <span>{food.cooking_time}</span>
          </div>
          <div className="flex items-center gap-2 text-sm text-slate-600">
            <ChefHat className="w-4 h-4 text-slate-500" />
            <span>{food.portion_size}</span>
          </div>
        </div>

        {/* Recipe Steps */}
        <div data-testid="food-recipe">
          <h3
            className="text-sm font-bold tracking-widest uppercase text-slate-600 mb-3"
            style={{ fontFamily: "Barlow Condensed, sans-serif" }}
          >
            Step-by-Step Recipe
          </h3>
          <ol className="space-y-2">
            {food.recipe.map((step, idx) => (
              <li key={idx} className="flex gap-3 text-sm">
                <span className="flex-shrink-0 w-6 h-6 rounded-full bg-[#84cc16]/10 text-[#84cc16] text-xs font-bold flex items-center justify-center">
                  {idx + 1}
                </span>
                <span className="text-slate-700 leading-relaxed">{step}</span>
              </li>
            ))}
          </ol>
        </div>
        </>
        )}
      </DialogContent>
    </Dialog>
  );
}
