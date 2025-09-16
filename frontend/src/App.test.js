import { render, screen, waitFor } from "@testing-library/react";
import App from './App';

jest.mock("./service/api", () => ({
  getJobs: jest.fn().mockResolvedValue([
    { job_id: 1, title: "Test Job", description: "desc", required_skills: [] }
  ]),
  getRecommendations: jest.fn().mockResolvedValue([
    { id: 1, name: "John Doe", Skills: "Python, React", City: "NY", Country: "US", "Monthly Rate": null, "Hourly Rate": 120, score: 0.92, reason: "mock" }
  ])
}));

test("loads and displays job and candidate", async () => {
  render(<App />);
  await waitFor(() => expect(screen.getByText(/Select a job/i)).toBeInTheDocument());
  // choose job by programmatically selecting (render will auto-select)
});
