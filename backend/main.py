
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import summarize_text

app = FastAPI(title="BERT Text Summarizer")

class SummarizeRequest(BaseModel):
    text: str
    num_sentences: int = 5

class SummarizeResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    try:
        summary = summarize_text(request.text, request.num_sentences)
        return SummarizeResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "BERT Summarizer API is running"}
