import { Info, Cog, BrainCircuit } from "lucide-react";

export default function ExplainabilityPanel({ data, modeInfo }) {
  const { rule_based_decisions, ml_assisted_insights } = data;

  return (
    <div className="glass-surface rounded-xl p-5" data-testid="explainability-panel">
      <div className="flex items-center gap-2 mb-4">
        <Info className="w-5 h-5 text-[#84cc16]" />
        <h2
          className="text-xl font-semibold tracking-tight uppercase text-slate-900"
          style={{ fontFamily: "Barlow Condensed, sans-serif" }}
        >
          Explainability (XAI)
        </h2>
      </div>

      {/* Mode Explanation */}
      <div className="rounded-lg bg-white/80 p-4 mb-4" data-testid="mode-explanation">
        <p className="text-xs font-bold tracking-widest uppercase text-slate-500 mb-2">
          Training Mode Decision
        </p>
        <p className="text-sm text-slate-700 leading-relaxed">{modeInfo.explanation}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Rule-Based Decisions */}
        <div data-testid="rule-decisions">
          <div className="flex items-center gap-2 mb-3">
            <Cog className="w-4 h-4 text-amber-400" />
            <h3 className="text-xs font-bold tracking-widest uppercase text-amber-400">
              Rule-Based Decisions
            </h3>
          </div>
          <div className="space-y-2">
            {rule_based_decisions.map((item, idx) => (
              <div
                key={idx}
                className="rounded-lg border border-slate-200 bg-white/70 p-3"
                data-testid={`rule-decision-${idx}`}
              >
                <p className="text-xs font-semibold text-slate-900 mb-1">{item.decision}</p>
                <p className="text-[11px] text-slate-500 leading-relaxed">{item.reason}</p>
              </div>
            ))}
          </div>
        </div>

        {/* ML-Assisted Insights */}
        <div data-testid="ml-decisions">
          <div className="flex items-center gap-2 mb-3">
            <BrainCircuit className="w-4 h-4 text-cyan-400" />
            <h3 className="text-xs font-bold tracking-widest uppercase text-cyan-400">
              ML-Assisted Insights
            </h3>
          </div>
          <div className="space-y-2">
            {ml_assisted_insights.map((item, idx) => (
              <div
                key={idx}
                className="rounded-lg border border-slate-200 bg-white/70 p-3"
                data-testid={`ml-insight-${idx}`}
              >
                <p className="text-xs font-semibold text-slate-900 mb-1">{item.insight}</p>
                <p className="text-[11px] text-slate-500 leading-relaxed">{item.reason}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
