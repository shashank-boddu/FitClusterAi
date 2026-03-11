import { Badge } from "@/components/ui/badge";
import { Flame, Scale, BatteryCharging } from "lucide-react";

const MODE_CONFIG = {
  performance: {
    color: "bg-red-500/10 text-red-400 border-red-500/30",
    glow: "shadow-[0_0_12px_-3px_rgba(239,68,68,0.4)]",
    icon: Flame,
  },
  balanced: {
    color: "bg-cyan-500/10 text-cyan-400 border-cyan-500/30",
    glow: "shadow-[0_0_12px_-3px_rgba(6,182,212,0.4)]",
    icon: Scale,
  },
  recovery: {
    color: "bg-emerald-500/10 text-emerald-400 border-emerald-500/30",
    glow: "shadow-[0_0_12px_-3px_rgba(16,185,129,0.4)]",
    icon: BatteryCharging,
  },
};

export default function ModeBadge({ mode, label }) {
  const config = MODE_CONFIG[mode] || MODE_CONFIG.balanced;
  const Icon = config.icon;

  return (
    <Badge
      variant="outline"
      className={`${config.color} ${config.glow} px-3 py-1.5 text-xs font-bold tracking-wider uppercase transition-all duration-300`}
      data-testid={`mode-badge-${mode}`}
    >
      <Icon className="w-3.5 h-3.5 mr-1.5" />
      {label}
    </Badge>
  );
}
