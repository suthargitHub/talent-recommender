import React, { useEffect, useState } from "react";
import { getJobs, getRecommendations } from "./services/api";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [selectedJob, setSelectedJob] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchJobs = async () => {
      const jobsData = await getJobs();
      setJobs(jobsData);
    };
    fetchJobs();
  }, []);

  const handleJobChange = async (e) => {
    const jobId = parseInt(e.target.value);
    setSelectedJob(jobId);
    setRecommendations([]);
    if (jobId) {
      setLoading(true);
      const recs = await getRecommendations(jobId, 10);
      setRecommendations(recs);
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header>
        <h1>Talent Recommendation System</h1>
      </header>

      <div className="job-selection">
        <label>Select a job:</label>
        <select value={selectedJob || ""} onChange={handleJobChange}>
          <option value="">-- Choose job posting --</option>
          {jobs.map((job) => (
            <option key={job.job_id} value={job.job_id}>
              {job.title}
            </option>
          ))}
        </select>
      </div>

      {loading && <p className="loading">Loading recommendations...</p>}

      {recommendations.length > 0 && (
        <div className="recommendations">
          <h2>Top Recommendations</h2>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Skills</th>
                <th>City</th>
                <th>Country</th>
                <th>Monthly Rate</th>
                <th>Hourly Rate</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {recommendations.map((rec) => (
                <tr key={rec.id}>
                  <td>{rec.name}</td>
                  <td>{rec.Skills}</td>
                  <td>{rec.City}</td>
                  <td>{rec.Country}</td>
                  <td>{rec["Monthly Rate"] || "-"}</td>
                  <td>{rec["Hourly Rate"] || "-"}</td>
                  <td>{rec.score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;
