from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("../model")

def summarize_text(text: str, num_sentences: int = 3) -> str:
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    if len(sentences) <= 2:
        return text

    embeddings = model.encode(sentences)
    doc_embedding = embeddings.mean(axis=0)

    scores = np.dot(embeddings, doc_embedding) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(doc_embedding) + 1e-10
    )

    n = min(num_sentences, len(sentences))
    top_indices = sorted(np.argsort(scores)[-n:])
    summary = '. '.join([sentences[i] for i in top_indices]) + '.'
    return summary