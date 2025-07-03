import React, { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

function App() {
  const [topic, setTopic] = useState("");
  const [outputType, setOutputType] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!topic.trim()) return;

    setLoading(true);
    setOutputType("");
    setResult(null);

    try {
      const response = await axios.post("http://localhost:5000/run", {
        topic: topic.trim(),
      });

      const data = response.data;
      setOutputType(data.type);
      setResult(data.result);
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

  // Helper function to render content based on type
  const renderContent = (content) => {
    if (Array.isArray(content)) {
      return (
        <ul className="list-disc list-inside ml-4 mt-2 space-y-1">
          {content.map((item, index) => (
            <li key={index} className="text-gray-700">
              {item}
            </li>
          ))}
        </ul>
      );
    } else if (typeof content === "object" && content !== null) {
      return (
        <div className="bg-gray-100 p-3 rounded-md mt-2">
          <pre className="text-sm text-gray-700">
            {JSON.stringify(content, null, 2)}
          </pre>
        </div>
      );
    } else {
      return (
        <div className="mt-2 text-gray-700">
          <ReactMarkdown className="prose max-w-none">
            {content || "No information provided"}
          </ReactMarkdown>
        </div>
      );
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white rounded-2xl shadow-xl p-8 w-full max-w-3xl">
        <h1 className="text-2xl font-bold text-center mb-6 text-gray-800">
          🚀 Lead Generation Agent
        </h1>

        <label className="block mb-2 font-medium text-gray-700">
          📝 Project or Job Description
        </label>
        <textarea
          className="w-full p-4 border border-gray-300 rounded-lg mb-6 focus:outline-none focus:ring-2 focus:ring-blue-400"
          rows="5"
          placeholder="Describe your project or job requirement..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
        >
          {loading ? (
            <span className="flex items-center justify-center">
              <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Processing...
            </span>
          ) : (
            "Submit"
          )}
        </button>

        {outputType && (
          <div className="mt-6 text-gray-800">
            <p className="font-semibold text-lg">
              <span className="text-blue-700">📌 Analysis Type:</span> {outputType}
            </p>
          </div>
        )}

        {result && (
          <div className="mt-6">
            {result.error ? (
              <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded">
                <div className="flex">
                  <div className="flex-shrink-0">
                    <svg className="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clipRule="evenodd" />
                    </svg>
                  </div>
                  <div className="ml-3">
                    <p className="text-sm text-red-700">{result.message}</p>
                  </div>
                </div>
              </div>
            ) : (
              <div className="bg-gray-50 rounded-lg border border-gray-200 overflow-hidden">
                {/* Project Overview Section */}
                {result["Project Overview"] && (
                  <div className="p-5 border-b border-gray-200">
                    <h2 className="text-xl font-bold text-gray-800 mb-3 flex items-center">
                      <span className="bg-blue-100 text-blue-800 rounded-full p-2 mr-3">
                        📋
                      </span>
                      Project Overview
                    </h2>
                    <div className="pl-10">
                      {renderContent(result["Project Overview"])}
                    </div>
                  </div>
                )}

                {/* Core Features Section */}
                {result["Core Features"] && (
                  <div className="p-5 border-b border-gray-200">
                    <h2 className="text-xl font-bold text-gray-800 mb-3 flex items-center">
                      <span className="bg-blue-100 text-blue-800 rounded-full p-2 mr-3">
                        ⚙️
                      </span>
                      Core Features
                    </h2>
                    <div className="pl-10">
                      {renderContent(result["Core Features"])}
                    </div>
                  </div>
                )}

                {/* Design & Usability Section */}
                {result["Design & Usability"] && (
                  <div className="p-5 border-b border-gray-200">
                    <h2 className="text-xl font-bold text-gray-800 mb-3 flex items-center">
                      <span className="bg-blue-100 text-blue-800 rounded-full p-2 mr-3">
                        🎨
                      </span>
                      Design & Usability
                    </h2>
                    <div className="pl-10">
                      {renderContent(result["Design & Usability"])}
                    </div>
                  </div>
                )}

                {/* Device & Platform Preferences Section */}
                {result["Device & Platform Preferences"] && (
                  <div className="p-5 border-b border-gray-200">
                    <h2 className="text-xl font-bold text-gray-800 mb-3 flex items-center">
                      <span className="bg-blue-100 text-blue-800 rounded-full p-2 mr-3">
                        📱
                      </span>
                      Device & Platform Preferences
                    </h2>
                    <div className="pl-10">
                      {renderContent(result["Device & Platform Preferences"])}
                    </div>
                  </div>
                )}

                {/* User Roles Section */}
                {result["User Roles"] && (
                  <div className="p-5 border-b border-gray-200">
                    <h2 className="text-xl font-bold text-gray-800 mb-3 flex items-center">
                      <span className="bg-blue-100 text-blue-800 rounded-full p-2 mr-3">
                        👥
                      </span>
                      User Roles
                    </h2>
                    <div className="pl-10">
                      {renderContent(result["User Roles"])}
                    </div>
                  </div>
                )}

                {/* Questions & Ambiguities Section */}
                {result["questions or ambiguities"] && (
                  <div className="p-5">
                    <h2 className="text-xl font-bold text-gray-800 mb-3 flex items-center">
                      <span className="bg-blue-100 text-blue-800 rounded-full p-2 mr-3">
                        ❓
                      </span>
                      Questions & Ambiguities
                    </h2>
                    <div className="pl-10">
                      {renderContent(result["questions or ambiguities"])}
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;