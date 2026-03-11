import { useState } from "react";
import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "@/components/ui/sonner";
import LandingPage from "@/pages/LandingPage";
import Dashboard from "@/pages/Dashboard";

function App() {
  const [recommendation, setRecommendation] = useState(null);

  return (
    <div className="min-h-screen bg-white">
      <Toaster richColors position="top-right" />
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              recommendation ? (
                <Dashboard
                  data={recommendation}
                  onBack={() => setRecommendation(null)}
                />
              ) : (
                <LandingPage onResult={setRecommendation} />
              )
            }
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
