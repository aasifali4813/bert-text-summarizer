
# 📝 BERT Text Summarizer

Extractive text summarization using BERT embeddings + KMeans clustering.

## 🛠️ Tech Stack
- **Model:** BERT (paraphrase-MiniLM-L6-v2) fine-tuned on CNN/DailyMail
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Training:** Google Colab (T4 GPU)

## 🚀 Setup

git clone https://github.com/aasifali4813/bert-text-summarizer.git
cd bert-text-summarizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run

Terminal 1 - Backend:
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000

Terminal 2 - Frontend:
cd frontend
streamlit run app.py

Open: http://localhost:8501

## 📦 Model
Hosted on Hugging Face: https://huggingface.co/aasifali4813/bert-summarizer
