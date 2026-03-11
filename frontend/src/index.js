import React from "react";
import ReactDOM from "react-dom/client";
import "@/index.css";
import App from "@/App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
// 🔥 FORCE REMOVE EMERGENT BADGE (runtime kill)
const removeEmergent = () => {
  const iframes = document.querySelectorAll("iframe");
  iframes.forEach((iframe) => {
    if (iframe.src && iframe.src.includes("emergent")) {
      iframe.remove();
    }
  });

  const links = document.querySelectorAll("a");
  links.forEach((a) => {
    if (a.href && a.href.includes("emergent")) {
      a.remove();
    }
  });
};

// Run once page loads
window.addEventListener("load", removeEmergent);

// Keep watching (in case it reinjects)
setInterval(removeEmergent, 1000);
// 🔥 ZERO-FLASH EMERGENT KILL (Layer 2)
const killEmergent = () => {
  document.querySelectorAll("iframe, a, div").forEach((el) => {
    const src = el.src || el.href || "";
    const id = el.id || "";
    const cls = el.className || "";

    if (
      src.includes("emergent") ||
      src.includes("moctale") ||
      id.toLowerCase().includes("emergent") ||
      cls.toLowerCase().includes("emergent")
    ) {
      el.remove();
    }
  });
};

// Run immediately (before first paint if possible)
killEmergent();

// Observe DOM in real time
const observer = new MutationObserver(killEmergent);
observer.observe(document.documentElement, {
  childList: true,
  subtree: true,
});
