import React, { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

function App() {
  const [topic, setTopic] = useState("");
  const [outputType, setOutputType] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showCheckpointUI, setShowCheckpointUI] = useState(false);
  const [checkpointsSubmitted, setCheckpointsSubmitted] = useState(false);

  const [checkpoints, setCheckpoints] = useState({
    overview: false,
    features: false,
    roles: false,
    devices: false,
    design: false,
    questions: false,
    time: false,
    job_title: false,
    about_company: false,
    role_summary: false,
    responsibilities: false,
    required_skills: false,
    preferred_qualifications: false,
  });

  const checkpointLabels = {
    overview: "Project Overview",
    features: "Core Features",
    roles: "User Roles",
    devices: "Device & Platform Preferences",
    design: "Design & Usability",
    questions: "Questions or Ambiguities",
    time: "Time Requirements",
    job_title: "Job Title",
    about_company: "About the Company",
    role_summary: "Role Summary",
    responsibilities: "Key Responsibilities",
    required_skills: "Required Skills",
    preferred_qualifications: "Preferred Qualifications",
  };

  const handleCheckboxChange = (key) => {
    setCheckpoints((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const atLeastOneChecked = () =>
    Object.values(checkpoints).some((value) => value);

  const isProjectType = (type) => {
    const lower = type?.toLowerCase();
    return lower === "project" || lower === "project-based-job";
  };

  const isJobType = (type) => {
    const lower = type?.toLowerCase();
    return lower === "job" || lower === "job-based-project";
  };

  const handleInitialSubmit = async () => {
    if (!topic.trim()) return;

    setLoading(true);
    setOutputType("");
    setResult(null);
    setShowCheckpointUI(false);
    setCheckpointsSubmitted(false);

    try {
      const response = await axios.post("http://localhost:5000/run/init", {
        topic: topic.trim(),
      });

      const data = response.data;
      setOutputType(data.type);

      if (isProjectType(data.type) || isJobType(data.type)) {
        setShowCheckpointUI(true);
      }
    } catch (error) {
      setResult({
        error: true,
        message:
          error.response?.data?.message ||
          "An unexpected error occurred while contacting the backend.",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleCheckpointSubmit = async () => {
    const selectedCheckpoints = Object.entries(checkpoints)
      .filter(([_, checked]) => checked)
      .map(([key]) => checkpointLabels[key]);

    if (!atLeastOneChecked()) return;

    setLoading(true);
    setResult(null);

    try {
      const endpoint = isProjectType(outputType)
        ? "http://localhost:5000/run/checkpoints"
        : "http://localhost:5000/run/job";

      const response = await axios.post(endpoint, {
        topic: topic.trim(),
        checkpoints: selectedCheckpoints,
      });

      setResult(response.data.result);
      setCheckpointsSubmitted(true);
    } catch (error) {
      setResult({
        error: true,
        message:
          error.response?.data?.message ||
          "An error occurred during checkpoint submission.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white rounded-2xl shadow-xl p-8 w-full max-w-3xl">
        <textarea
          className="w-full p-4 border rounded mb-4"
          rows="4"
          placeholder="Describe your project or job..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />

        <button
          onClick={handleInitialSubmit}
          className="bg-blue-600 text-white py-2 px-4 rounded mb-4"
        >
          {loading ? "Processing..." : "Submit"}
        </button>

        {outputType && (
          <p className="mb-2 text-gray-700">Type: {outputType}</p>
        )}

        {showCheckpointUI && (
          <div className="bg-yellow-100 p-4 rounded mb-4">
            <p className="font-bold mb-2">Checklist</p>
            {Object.entries(checkpoints)
              .filter(([key]) =>
                isProjectType(outputType)
                  ? ["overview", "features", "roles", "devices", "design", "questions", "time"].includes(key)
                  : ["job_title", "about_company", "role_summary", "responsibilities", "required_skills", "preferred_qualifications"].includes(key)
              )
              .map(([key, value]) => (
                <label key={key} className="block">
                  <input
                    type="checkbox"
                    checked={value}
                    onChange={() => handleCheckboxChange(key)}
                    disabled={checkpointsSubmitted}
                  /> {checkpointLabels[key]}
                </label>
              ))}
            <button
              className="mt-3 bg-green-600 text-white px-4 py-2 rounded"
              disabled={!atLeastOneChecked() || loading || checkpointsSubmitted}
              onClick={handleCheckpointSubmit}
            >
              {checkpointsSubmitted ? "Submitted" : "Submit Checkpoints"}
            </button>
          </div>
        )}

        {result && (
          <div className="bg-gray-100 p-4 rounded">
            {Object.entries(result).map(([key, val]) => (
              <div key={key} className="mb-3">
                <h4 className="font-semibold text-blue-700">{key}</h4>
                <p>{val}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;