import { Flame } from "lucide-react";

export default function DietCard({ day, onFoodClick }) {
  return (
    <div data-testid={`diet-day-${day.day}`}>
      {/* Day Totals */}
      <div className="grid grid-cols-2 gap-2 mb-4">
        <div className="rounded-lg bg-white/80 p-2 text-center">
          <p className="text-xs text-slate-500 uppercase tracking-wider">Calories</p>
          <p className="text-base font-bold text-slate-900" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
            {day.total_calories}
          </p>
        </div>
        <div className="rounded-lg bg-white/80 p-2 text-center">
          <p className="text-xs text-slate-500 uppercase tracking-wider">Protein</p>
          <p className="text-base font-bold text-[#84cc16]" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
            {day.total_protein}g
          </p>
        </div>
      </div>

      {/* Meals */}
      <div className="space-y-2">
        {day.meals.map((meal, idx) => {
          const totalCals = meal.foods.reduce((s, f) => s + f.calories, 0);
          return (
            <div
              key={idx}
              className="rounded-lg border border-slate-200 bg-white/70 p-3"
              data-testid={`meal-${idx}`}
            >
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-[10px] font-bold tracking-widest uppercase text-slate-500">
                  {meal.meal_type}
                </span>
                <div className="flex items-center gap-1 text-[10px] text-slate-500">
                  <Flame className="w-3 h-3" />
                  {totalCals} kcal
                </div>
              </div>
              <div className="space-y-1.5">
                {meal.foods.map((food, fIdx) => (
                  <button
                    key={fIdx}
                    onClick={() => onFoodClick(food)}
                    className="w-full text-left hover:bg-[#84cc16]/5 rounded-md p-1.5 -mx-1.5 transition-all duration-300 group"
                    data-testid={`food-${food.id}`}
                  >
                    <p className="text-sm font-medium text-slate-900 group-hover:text-[#84cc16] transition-colors truncate">
                      {food.name}
                    </p>
                    <div className="flex gap-3 mt-0.5">
                      <span className="text-[10px] text-slate-500">P: {food.protein}g</span>
                      <span className="text-[10px] text-slate-500">C: {food.carbs}g</span>
                      <span className="text-[10px] text-slate-500">F: {food.fat}g</span>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
