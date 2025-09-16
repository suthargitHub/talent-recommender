import os
from typing import List
import numpy as np

PROVIDER = os.getenv("EMBEDDING_PROVIDER", "sbert").lower()

if PROVIDER == "sbert":
    from sentence_transformers import SentenceTransformer
    MODEL_NAME = os.getenv("SBERT_MODEL", "all-MiniLM-L6-v2")
    _model = SentenceTransformer(MODEL_NAME)

    def embed_texts(texts: List[str]) -> List[List[float]]:
        # accepts list of texts and returns list of vectors (as lists)
        if isinstance(texts, str):
            texts = [texts]
        embeddings = _model.encode(texts, show_progress_bar=False)
        return [emb.tolist() for emb in embeddings]

elif PROVIDER == "openai":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

    def embed_texts(texts: List[str]) -> List[List[float]]:
        if isinstance(texts, str):
            texts = [texts]
        # chunk if many texts
        results = []
        for t in texts:
            resp = openai.Embedding.create(model=OPENAI_MODEL, input=t)
            vec = resp["data"][0]["embedding"]
            results.append(vec)
        return results

else:
    # fallback: very simple TF-IDF vectorization (not true embeddings)
    from sklearn.feature_extraction.text import TfidfVectorizer
    _tfidf = TfidfVectorizer(max_features=1024)

    # we will fit lazily when used
    _is_fitted = False
    _corpus_for_fit = []

    def embed_texts(texts: List[str]) -> List[List[float]]:
        global _is_fitted, _tfidf
        if not _is_fitted:
            _corpus_for_fit.extend(texts)
            _tfidf.fit(_corpus_for_fit)
            _is_fitted = True
        vecs = _tfidf.transform(texts).toarray()
        return [v.tolist() for v in vecs]
