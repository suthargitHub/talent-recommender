Project Documentation – Talent Recommendation System


1. Overview
This project is a Generative AI-powered recruitment recommendation system.
It matches job postings with candidate profiles using embeddings and similarity scoring, providing recruiters with the Top 10 ranked candidates for each role.



2. Objectives
Automate candidate shortlisting using AI.
Provide recruiters with a simple, intuitive web interface.
Integrate embeddings/LLMs to compare job descriptions with candidate bios.
Deliver an end-to-end deployed proof-of-concept within limited time.


3. Tech Stack
Backend: Python, Flask, Gunicorn
Frontend: React, Tailwind CSS (dark theme UI)
AI/ML: Embeddings (sentence-transformers, Gemini API, or OpenAI API)
Dataset: Provided talent.csv
Deployment: Render (backend), Vercel/Netlify (frontend)


4. System Architecture
Recruiter UI (React) ──► Flask API (Python) ──► Embedding Model
                                   │
                                   ▼
                            Candidate Dataset (CSV)
                                   │
                                   ▼
                      Ranked Candidate List (Top 10)

5. Features
Job Role Selection → Recruiter selects a job from dropdown.
Top 10 Candidate Ranking → Candidates scored by similarity.
Dark Theme, Minimal UI → Optimized for recruiters.

Extendable Matching:
🐾 Hobby-based matching (e.g., "animals" → animal content creators).
🌍 Language-based matching.
📊 Sentiment/creativity analysis.


6. Setup Guide
Clone Repository
git clone https://github.com/suthargitHub/talent-recommender.git
cd talent-recommender

Backend Setup
cd backend
pip install -r requirements.txt
python app.py

Backend runs at: http://localhost:5000

Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs at: http://localhost:3000



7. Usage
Open the frontend in a browser (local or deployed link).
Select a job posting from the dropdown.
Backend API computes embeddings & similarity.
The UI displays Top 10 ranked candidates with scores.
Optional: recruiters can view all ranked candidates.



8. Evaluation Criteria
Recruiters can assess this project on:
✅ Technical fluency (Python + Flask backend, React frontend).
✅ Integration skills (frontend ↔ backend API).
✅ Generative AI usage (embeddings for recommendations).
✅ Code organization & comments.
✅ Documentation & communication.
✅ Creativity (extra features beyond basics).



9. Future Scope
Resume parsing (PDF/DOCX → embeddings).
ATS (Applicant Tracking System) integration.
Vector database (Pinecone, FAISS) for large-scale candidate search.
Advanced filters (experience, location, skills).
Explainable AI → “why was this candidate ranked higher?”.



10. Repository Structure
talent-recommender/
│── backend/
│   ├── app.py
│   ├── models/
│   │   └── embedding.py
│   ├── utils.py
│   └── requirements.txt
│
│── data/
│   └── talent.csv
│
│── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── service/api.js
│   └── package.json
│
│── tests/
│   └── test_recommender.py
│
│── docs/
│   └── documentation.md
│
│── README.md