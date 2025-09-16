const BASE_URL = "http://localhost:5000"; // Make sure Flask is running on port 5000

export const getJobs = async () => {
  try {
    const response = await fetch(`${BASE_URL}/jobs`);
    if (!response.ok) {
      throw new Error("Failed to fetch jobs");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching jobs:", error);
    return [];
  }
};

export const getRecommendations = async (jobId, topN = 10) => {
  try {
    const response = await fetch(`${BASE_URL}/recommend/${jobId}?top_n=${topN}`);
    if (!response.ok) {
      throw new Error("Failed to fetch recommendations");
    }
    const data = await response.json();
    return data.results || [];
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    return [];
  }
};
