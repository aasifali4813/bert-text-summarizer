# 📝 BERT Text Summarizer

An extractive text summarization system that uses BERT sentence embeddings to identify and extract the most important sentences from any given text.

## 🔗 Links
- 🤗 **HuggingFace Model:** [aasifali4813/bert-summarizer](https://huggingface.co/aasifali4813/bert-summarizer)
- 💻 **GitHub Repo:** [aasifali4813/bert-text-summarizer](https://github.com/aasifali4813/bert-text-summarizer)

## 🛠️ Tech Stack
| Component | Technology |
|-----------|-----------|
| **Model** | paraphrase-MiniLM-L6-v2 (fine-tuned) |
| **Backend** | FastAPI |
| **Frontend** | Streamlit |
| **Training** | Google Colab (T4 GPU) |
| **Dataset** | CNN/DailyMail (5000 samples) |
| **Model Hosting** | Hugging Face Hub |

## 🧠 How It Works
```
Input Text → Split into Sentences → BERT Embeddings → 
Cosine Similarity → Rank Sentences → Top N Sentences → Summary
```

## 🚀 Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/aasifali4813/bert-text-summarizer.git
cd bert-text-summarizer
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Run the App

### Terminal 1 — Backend
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Terminal 2 — Frontend
```bash
cd frontend
streamlit run app.py
```

### Open in browser
```
http://localhost:8501
```

## 📁 Project Structure
```
bert-text-summarizer/
├── backend/
│   ├── main.py        # FastAPI app
│   └── model.py       # BERT summarizer logic
├── frontend/
│   └── app.py         # Streamlit UI
├── model/             # Local model files
├── requirements.txt
├── .gitignore
└── README.md
```

## 📦 Model Details
- **Base Model:** sentence-transformers/paraphrase-MiniLM-L6-v2
- **Fine-tuned on:** CNN/DailyMail dataset
- **Model Size:** 22.7M parameters (~90MB)
- **Output:** 384-dimensional sentence embeddings
- **Loss Function:** MultipleNegativesRankingLoss
- **HuggingFace:** [aasifali4813/bert-summarizer](https://huggingface.co/aasifali4813/bert-summarizer)

## 🖥️ API Endpoint
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/summarize` | Summarize input text |
| GET | `/` | API health check |
| GET | `/docs` | Swagger UI |

### Example Request
```json
{
  "text": "Your long text here...",
  "num_sentences": 3
}
```

### Example Response
```json
{
  "summary": "Most important sentences extracted from the text."
}
```