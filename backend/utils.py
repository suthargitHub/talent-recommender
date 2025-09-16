import numpy as np
import re

def safe_text(x):
    if x is None: return ""
    return str(x)

def cosine_sim(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)

def normalize_minmax(scores):
    arr = np.array(scores, dtype=float)
    if arr.max() - arr.min() == 0:
        return [0.0 for _ in arr]
    normalized = (arr - arr.min()) / (arr.max() - arr.min())
    return normalized.tolist()

def extract_skill_set(skill_text):
    # simple splitter; you can improve tokenization
    if not skill_text:
        return set()
    tokens = re.split(r'[,;/\|]+|\s+-\s+', skill_text)
    tokens = [t.strip().lower() for t in tokens if t.strip()]
    return set(tokens)
