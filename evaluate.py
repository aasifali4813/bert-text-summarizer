from rouge_score import rouge_scorer
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("./model")

def summarize_text(text, num_sentences=3):
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
    return '. '.join([sentences[i] for i in top_indices]) + '.'

articles = [
    "Artificial intelligence is transforming the world. Machine learning algorithms perform complex tasks. Deep learning has revolutionized image recognition. Neural networks process vast amounts of data. Companies are investing heavily in AI research.",
    "Climate change is affecting global weather patterns. Rising temperatures are melting polar ice caps. Sea levels are increasing around the world. Extreme weather events are becoming more frequent. Governments are working on solutions.",
]

references = [
    "Artificial intelligence is transforming the world. Companies are investing heavily in AI research.",
    "Climate change is affecting global weather patterns. Governments are working on solutions.",
]

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

r1, r2, rl = [], [], []
for article, reference in zip(articles, references):
    prediction = summarize_text(article, num_sentences=2)
    scores = scorer.score(reference, prediction)
    r1.append(scores['rouge1'].fmeasure)
    r2.append(scores['rouge2'].fmeasure)
    rl.append(scores['rougeL'].fmeasure)

print(f"ROUGE-1: {np.mean(r1):.4f}")
print(f"ROUGE-2: {np.mean(r2):.4f}")
print(f"ROUGE-L: {np.mean(rl):.4f}")
