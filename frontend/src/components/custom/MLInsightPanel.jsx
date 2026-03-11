import { BrainCircuit, Users, BarChart3 } from "lucide-react";
import {
  ResponsiveContainer,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  Radar,
} from "recharts";

export default function MLInsightPanel({ insights }) {
  // Transform feature importance for radar chart
  const radarData = Object.entries(insights.feature_importance).map(
    ([key, val]) => ({
      feature: key,
      value: Math.round(val * 100),
    })
  );

  return (
    <div className="glass-surface rounded-xl p-5" data-testid="ml-insights-panel">
      <div className="flex items-center gap-2 mb-4">
        <BrainCircuit className="w-5 h-5 text-[#84cc16]" />
        <h2
          className="text-xl font-semibold tracking-tight uppercase text-slate-900"
          style={{ fontFamily: "Barlow Condensed, sans-serif" }}
        >
          ML-Assisted Insights
        </h2>
        <span className="text-[10px] px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 font-bold tracking-wider uppercase ml-auto">
          Pattern Discovery
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Cluster Info */}
        <div className="space-y-3">
          <div className="rounded-lg bg-white/80 p-4" data-testid="cluster-info">
            <p className="text-xs font-bold tracking-widest uppercase text-slate-500 mb-1">
              User Persona (Cluster {insights.cluster_id})
            </p>
            <p className="text-base font-bold text-slate-900" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
              {insights.cluster_label}
            </p>
            <p className="text-xs text-slate-600 mt-1 leading-relaxed">
              {insights.cluster_description}
            </p>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div className="rounded-lg bg-white/80 p-3" data-testid="confidence-score">
              <p className="text-xs text-slate-500 uppercase tracking-wider mb-1">Confidence</p>
              <p className="text-xl font-bold text-[#84cc16]" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
                {(insights.confidence * 100).toFixed(0)}%
              </p>
              <div className="w-full h-1.5 bg-slate-200 rounded-full mt-2">
                <div
                  className="h-full bg-[#84cc16] rounded-full transition-all duration-500"
                  style={{ width: `${insights.confidence * 100}%` }}
                />
              </div>
            </div>
            <div className="rounded-lg bg-white/80 p-3" data-testid="similarity-score">
              <div className="flex items-center gap-1 mb-1">
                <Users className="w-3 h-3 text-slate-500" />
                <p className="text-xs text-slate-500 uppercase tracking-wider">Similarity</p>
              </div>
              <p className="text-xl font-bold text-cyan-400" style={{ fontFamily: "Barlow Condensed, sans-serif" }}>
                {(insights.similarity_score * 100).toFixed(0)}%
              </p>
              <p className="text-[10px] text-slate-500 mt-1">
                vs {insights.similar_profiles_count} profiles
              </p>
            </div>
          </div>

          <div className="rounded-lg bg-[#84cc16]/5 border border-[#84cc16]/20 p-3">
            <p className="text-xs font-bold tracking-widest uppercase text-[#84cc16] mb-1">
              Cluster Recommendation
            </p>
            <p className="text-xs text-slate-700 leading-relaxed">
              {insights.cluster_recommendation}
            </p>
          </div>
        </div>

        {/* Radar Chart */}
        <div className="flex flex-col" data-testid="feature-importance-chart">
          <div className="flex items-center gap-1 mb-2">
            <BarChart3 className="w-3.5 h-3.5 text-slate-500" />
            <p className="text-xs font-bold tracking-widest uppercase text-slate-500">
              Feature Importance
            </p>
          </div>
          <div className="flex-1 min-h-[220px]">
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart cx="50%" cy="50%" outerRadius="70%" data={radarData}>
                <PolarGrid stroke="#27272a" />
                <PolarAngleAxis
                  dataKey="feature"
                  tick={{ fill: "#71717a", fontSize: 10 }}
                />
                <Radar
                  name="Importance"
                  dataKey="value"
                  stroke="#84cc16"
                  fill="#84cc16"
                  fillOpacity={0.15}
                  strokeWidth={2}
                />
              </RadarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
