import React, { useState } from "react";
import axios from "axios";
import "./App.css";

// API configuration
const API_BASE_URL = "https://doccompare-ss5b.onrender.com";

function App() {
  const [documents, setDocuments] = useState([]);
  const [similarityScore, setSimilarityScore] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setDocuments((prev) => [
        ...prev,
        {
          filename: response.data.filename,
          content: response.data.processed_doc,
        },
      ]);
    } catch (err) {
      setError("Error uploading file: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const compareDocuments = async () => {
    if (documents.length < 2) {
      setError("Please upload at least two documents to compare");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/compare`, {
        doc1: documents[0].content,
        doc2: documents[1].content,
      });

      setSimilarityScore(response.data.similarity_score);
    } catch (err) {
      setError("Error comparing documents: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Document Similarity Checker</h1>
      </header>

      <main className="App-main">
        <div className="upload-section">
          <h2>Upload Documents</h2>
          <input
            type="file"
            onChange={handleFileUpload}
            accept=".txt,.pdf,.doc,.docx"
            disabled={loading}
          />
        </div>

        <div className="documents-list">
          <h2>Uploaded Documents</h2>
          <ul>
            {documents.map((doc, index) => (
              <li key={index}>{doc.filename}</li>
            ))}
          </ul>
        </div>

        {documents.length >= 2 && (
          <button
            className="compare-button"
            onClick={compareDocuments}
            disabled={loading}
          >
            Compare Documents
          </button>
        )}

        {similarityScore !== null && (
          <div className="result-section">
            <h2>Similarity Score</h2>
            <div className="score-display">
              {Math.round(similarityScore * 100)}%
            </div>
          </div>
        )}

        {loading && <div className="loading">Processing...</div>}
        {error && <div className="error">{error}</div>}
      </main>
    </div>
  );
}

export default App;
