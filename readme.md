# 📘 Enterprise GenAI Knowledge Assistant (RAG-based Q&A System)

Production-style **Generative AI knowledge assistant** built using **Retrieval-Augmented Generation (RAG)** to answer natural-language questions over enterprise documents such as HR policies and manuals.

This project is designed as a **portfolio piece for a GenAI / AI Engineer role**. It demonstrates document ingestion, semantic search, vector databases, prompt-grounded LLM responses, conversational memory, and deployment via a FastAPI backend.

---

## 🧠 Problem Statement

Enterprises store critical knowledge across large volumes of unstructured documents (HR policies, SOPs, manuals). Traditional keyword search is slow, brittle, and fails to understand user intent.

### Goal:
Build an end-to-end GenAI system that:

- Answers employee questions in natural language  
- Grounds responses strictly in internal documents  
- Provides source citations for trust and explainability  
- Supports follow-up questions via conversational memory  
- Exposes the system through a production-ready API  

---

## 🗂️ Project Structure

```text
.
├── api/
│   └── main.py              # FastAPI entry point
├── rag/
│   ├── qa_chain.py          # Core RAG pipeline (retrieval + generation)
│   ├── memory.py            # Conversational memory (in-memory buffer)
│   └── prompts.py           # Prompt templates
├── ingestion/
│   └── ingest_docs.py       # Document ingestion & chunking
├── vectorstore/
│   └── chroma_store.py      # ChromaDB setup and persistence
├── data/
│   └── HR_Policy_Manual.pdf # Sample enterprise document
├── venv/                    # Python virtual environment
├── requirements.txt
└── README.md

##🧰 Tech Stack
Language:
Python

GenAI / Orchestration:
LangChain

LLMs & Embeddings:
Hugging Face Transformers, Sentence-Transformers, FLAN-T5

Vector Database:
ChromaDB

Search & Retrieval:
Semantic Vector Search, Multi-Query Expansion

Serving / Backend:
FastAPI, Uvicorn

Memory:
In-memory conversational memory

Environment & Tools:
Python venv, VS Code, Git, GitHub

## 🏗️ System Architecture Overview
The system follows a standard Retrieval-Augmented Generation (RAG) workflow:

Enterprise documents are ingested and split into semantic chunks

Each chunk is converted into vector embeddings using Hugging Face models

Embeddings are stored in ChromaDB for efficient similarity search

User queries are embedded and matched against stored vectors

Relevant document chunks are retrieved and injected into the prompt

A local LLM generates answers strictly grounded in retrieved context

Source citations (document + page) are returned with each response

FastAPI exposes the pipeline as a production-ready REST API

## 🔍 RAG Pipeline Details
Document Ingestion & Chunking
PDFs are loaded using LangChain document loaders

Text is split using recursive chunking with overlap

Metadata (document name, page number) is preserved for traceability

Embedding & Vector Storage
Sentence-transformer models generate dense semantic embeddings

ChromaDB stores embeddings and supports fast similarity search

Retrieval & Query Expansion
User queries are expanded using multi-query expansion

Results are deduplicated to improve retrieval recall and coverage

Prompting & Generation
Retrieved chunks are injected into a strict prompt template

The LLM is instructed to answer only from provided context

This significantly reduces hallucinations

## 🌐 FastAPI Backend
The system is exposed via a FastAPI service.

Available Endpoints
1. Health Check
bash
Copy code
GET /health
Response:

json
Copy code
{ "status": "ok" }
2. Ask a Question
bash
Copy code
POST /ask
Request:

json
Copy code
{
  "question": "What is the casual leave policy?"
}
Response:

json
Copy code
{
  "answer": "Casual leave can be taken while on tour...",
  "sources": [
    {
      "source": "HR_Policy_Manual.pdf",
      "page": 79
    }
  ]
}

## 🧠 Conversational Memory
Stores recent user–assistant interactions in application memory (RAM)

Enables follow-up questions such as:

“What about half-day leave?”

Implemented as a lightweight, session-based buffer

Suitable for demos; can be replaced with Redis/DB in production

## 🏃 How to Run Locally
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/genai-knowledge-assistant.git
cd genai-knowledge-assistant
Create & Activate Virtual Environment
Windows

bash
Copy code
python -m venv venv
venv\Scripts\activate
Linux / macOS

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Run Document Ingestion
bash
Copy code
python ingestion/ingest_docs.py
Run FastAPI Backend
bash
Copy code
uvicorn api.main:app --reload
Open in browser:

API Docs: http://127.0.0.1:8000/docs

## ⚖️ Design Trade-offs
Used open-source local models instead of paid APIs for cost and data privacy

In-memory conversational memory for simplicity and clarity

Vector-only search (hybrid search identified as a future enhancement)

CPU-based inference for accessibility (GPU recommended for production)

## 🚀 Possible Extensions
Hybrid search (BM25 + vector search)

Reranking models for improved retrieval precision

Persistent memory using Redis or a database

Authentication and role-based access control

UI layer using Streamlit or React

GPU-accelerated inference

## 📌 Use Cases
HR policy assistants

Internal enterprise knowledge bases

Employee self-service portals

Compliance and audit support tools

Document intelligence systems

⭐ Final Note
Built an end-to-end enterprise GenAI system covering document ingestion, semantic retrieval, prompt-grounded generation, conversational memory, and API deployment.


## 👤 Author
Subhash Chandra Bose Muda
