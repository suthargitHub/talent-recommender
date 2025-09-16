# Talent Recommender System  

A full-stack project that recommends the **top 10 candidates** for a given job description using **embeddings** and similarity scoring.  

## 🚀 Features
- Backend (Flask API)  
- Frontend (React)  
- Embedding model for candidate–job similarity  
- Job–Candidate recommendation with top matches  
- REST API endpoints for integration  

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask, Flask-CORS, scikit-learn, sentence-transformers  
- **Frontend**: React, Axios  
- **Database**: CSV files (talent.csv, jobs.csv)  

---

## 📂 Project Structure
├── backend
│ ├── app.py # Flask backend
│ ├── requirements.txt # Backend dependencies
│ ├── models/
│ │ └── embedding.py # Embedding functions
│ ├── recommender.py # Recommendation logic
│ └── data/
│ ├── talent.csv
│ └── jobs.csv
│
└── frontend
├── package.json # Frontend dependencies
├── src/
│ ├── App.js
│ ├── components/
│ └── services/api.js


---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository
```bash```
git clone https://github.com/<your-username>/talent-recommender.git
cd talent-recommender


2️⃣ Run the Backend (Flask API)
cd backend
python -m venv venv
venv\Scripts\activate    # (Windows)

pip install -r requirements.txt
python app.py


API will run on:
http://127.0.0.1:5000


✅ Test it by visiting in browser:
http://127.0.0.1:5000/jobs

3️⃣ Run the Frontend (React)
Open a new terminal:

cd frontend
npm install
npm --prefix frontend start


React app will start on:
http://localhost:3000

🌐 API Endpoints
Endpoint	Method	Description
/jobs	GET	Get all jobs
/recommendations/<job_id>	GET	Get top 10 candidates for a job

Example:
http://127.0.0.1:5000/recommendations/1

📸 Screenshots 
<img width="1485" height="544" alt="image" src="https://github.com/user-attachments/assets/90381f9a-5bdf-44f8-876f-0575840b4306" />
<img width="909" height="416" alt="image" src="https://github.com/user-attachments/assets/e2a4a19d-089c-410f-95b2-9b7c51ca414c" />


📌 System Requirements
Python 3.9 / 3.10
Node.js 18+
npm 8+


👨‍💻 Author
Developed by Dheeraj Kumar

LinkedIn-www.linkedin.com/in/dheeraj-kumar-64889924a
GitHub-https://github.com/suthargitHub
