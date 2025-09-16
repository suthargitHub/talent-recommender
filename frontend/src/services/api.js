export const getJobs = async () => {
  const resp = await fetch("http://localhost:5000/jobs");
  return resp.json();
};

export const getRecommendations = async (jobId, topN = 10) => {
  const resp = await fetch(`http://localhost:5000/recommend/${jobId}?top_n=${topN}`);
  if (!resp.ok) throw new Error("Failed to fetch recommendations");
  const data = await resp.json();
  return data.results;
};
