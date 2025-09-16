import os
import pandas as pd
from models.embeddings import embed_texts
from utils import cosine_sim, extract_skill_set
from jobs import get_job_by_id, list_jobs

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "talent_samples.csv")

# Load candidate data
df = pd.read_csv(DATA_PATH)
df["First Name"] = df.get("First Name", "").fillna("")
df["Last Name"] = df.get("Last Name", "").fillna("")
df["Skills"] = df.get("Skills", "").fillna("").astype(str)
df["Profile Description"] = df.get("Profile Description", "").fillna("").astype(str)
df["City"] = df.get("City", "").fillna("").astype(str)
df["Country"] = df.get("Country", "").fillna("").astype(str)
df["Monthly Rate"] = pd.to_numeric(df.get("Monthly Rate", pd.Series([None]*len(df))), errors="coerce")
df["Hourly Rate"] = pd.to_numeric(df.get("Hourly Rate", pd.Series([None]*len(df))), errors="coerce")
df["Gender"] = df.get("Gender", "").fillna("").astype(str)
df["id"] = df.index + 1
df["name"] = (df["First Name"].str.strip() + " " + df["Last Name"].str.strip()).str.strip()

# Build profile text for embeddings
concat_cols = ["Skills", "Profile Description", "Job Types", "Content Verticals", "Past Creators"]
for c in concat_cols:
    if c not in df.columns:
        df[c] = ""
df["profile_text"] = df[concat_cols].fillna("").agg(" ".join, axis=1).astype(str)

# Compute embeddings for candidates
df["embedding"] = embed_texts(df["profile_text"].tolist())
df["skill_set"] = df["Skills"].apply(lambda s: extract_skill_set(s))

# Weights for scoring
WEIGHTS = {"embed": 0.6, "skill": 0.2, "rules": 0.2}
ASIAN_COUNTRIES = set([
    "india","china","japan","south korea","singapore","thailand","vietnam","indonesia",
    "philippines","malaysia","pakistan","bangladesh","nepal","sri lanka","bhutan"
])

def score_candidate_for_job(job, job_embedding, candidate_row):
    emb_sim = cosine_sim(job_embedding, candidate_row["embedding"])
    job_skills = [s.lower().strip() for s in job.get("required_skills", [])]
    candidate_skills = candidate_row["skill_set"]
    overlap = sum(1 for s in job_skills if any(s in cs or cs in s for cs in candidate_skills))
    skill_score = overlap / max(1, len(job_skills))

    # Location score
    loc_score = 0.0
    if job.get("preferred_locations"):
        pref = [p.lower() for p in job["preferred_locations"] if p]
        cand_city = (candidate_row.get("City","") or "").lower()
        cand_country = (candidate_row.get("Country","") or "").lower()
        if any(p in cand_city or p in cand_country for p in pref):
            loc_score = 1.0
        if "asia" in pref and cand_country in ASIAN_COUNTRIES:
            loc_score = max(loc_score, 1.0)

    # Budget score
    budget_score = 0.5
    if job.get("rate_type") == "monthly" and job.get("budget"):
        br = job["budget"]
        cand_rate = candidate_row.get("Monthly Rate")
        if pd.notna(cand_rate):
            budget_score = 1.0 if cand_rate <= br else max(0.0, 1 - (cand_rate - br) / (br*2))
    elif job.get("rate_type") == "hourly" and job.get("budget"):
        low, high = job["budget"] if isinstance(job["budget"], list) else (job["budget"], job["budget"])
        cand_rate = candidate_row.get("Hourly Rate")
        if pd.notna(cand_rate):
            if low <= cand_rate <= high:
                budget_score = 1.0
            else:
                diff = min(abs(cand_rate - low), abs(cand_rate - high))
                budget_score = max(0.0, 1 - (diff / max(1, (low or 1))))

    # Gender preference bonus
    gender_bonus = 0.0
    if job.get("gender_preference"):
        pref = (job["gender_preference"] or "").lower()
        if pref and pref in (candidate_row.get("Gender","") or "").lower():
            gender_bonus = 0.05

    rules_score = (loc_score * 0.5) + (budget_score * 0.4) + gender_bonus
    final = WEIGHTS["embed"] * emb_sim + WEIGHTS["skill"] * skill_score + WEIGHTS["rules"] * rules_score
    reason = f"embed={emb_sim:.3f},skill={skill_score:.2f},loc={loc_score:.2f},budget={budget_score:.2f},gender_bonus={gender_bonus:.2f}"
    return final, reason

def build_job_embedding(job):
    parts = [" ".join(job.get("required_skills", [])), job.get("title",""), job.get("description","")]
    job_text = " ".join([p for p in parts if p])
    return embed_texts([job_text])[0]

def recommend_for_job(job_id: int, top_n: int = 10):
    job = get_job_by_id(job_id)
    if not job:
        raise ValueError("Job not found")
    job_emb = build_job_embedding(job)
    scores = []
    for _, row in df.iterrows():
        sc, reason = score_candidate_for_job(job, job_emb, row)
        scores.append((row["id"], row["name"], row["Skills"], row["City"], row["Country"],
                       row.get("Monthly Rate"), row.get("Hourly Rate"), sc, reason))
    sorted_scores = sorted(scores, key=lambda x: x[7], reverse=True)
    top = sorted_scores[:top_n]
    results = []
    for cand in top:
        results.append({
            "id": int(cand[0]),
            "name": cand[1],
            "Skills": cand[2],
            "City": cand[3],
            "Country": cand[4],
            "Monthly Rate": cand[5] if pd.notna(cand[5]) else None,
            "Hourly Rate": cand[6] if pd.notna(cand[6]) else None,
            "score": round(float(cand[7]), 4),
            "reason": cand[8]
        })
    return results

def get_jobs_meta():
    return list_jobs()
