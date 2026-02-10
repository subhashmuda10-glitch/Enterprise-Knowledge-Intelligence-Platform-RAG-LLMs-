from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

from rag.qa_chain import ask_question

# -----------------------------
# FastAPI App Initialization
# -----------------------------

app = FastAPI(
    title="Enterprise GenAI Knowledge Assistant",
    description="RAG-based Question Answering system over enterprise documents",
    version="1.0.0"
)

# -----------------------------
# Request & Response Schemas
# -----------------------------

class QueryRequest(BaseModel):
    question: str


class Source(BaseModel):
    source: str | None = None
    page: int | None = None


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]

# -----------------------------
# Health Check Endpoint
# -----------------------------

@app.get("/health")
def health_check():
    """
    Simple health check endpoint
    """
    return {"status": "ok"}

# -----------------------------
# Main RAG Endpoint
# -----------------------------

@app.post("/ask", response_model=QueryResponse)
def ask_question_api(request: QueryRequest):
    """
    Ask a question to the RAG system
    """
    answer, docs = ask_question(request.question)

    sources = []
    for doc in docs:
        sources.append(
            {
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page")
            }
        )

    return {
        "answer": answer,
        "sources": sources
    }
