# 📘 Enterprise GenAI Knowledge Assistant (RAG-based Q&A System)

An enterprise-grade **Generative AI knowledge assistant** built using **Retrieval-Augmented Generation (RAG)** to enable accurate, explainable, and context-aware question answering over internal documents such as HR policies and manuals.

This system combines **semantic search** with **LLM-based generation**, ensuring answers are grounded in source documents and suitable for enterprise use cases.

---

## 🚀 Key Features

- 📄 Natural language Q&A over enterprise documents (PDFs)
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- 🔁 Multi-query expansion for improved retrieval coverage
- 💬 Conversational memory for multi-turn interactions
- 📚 Source citations with document and page references
- ⚡ FastAPI backend with RESTful endpoints
- 🔐 Designed with enterprise explainability and trust in mind

---

## 🏗️ System Architecture (High-Level)

1. Documents are ingested and split into semantic chunks  
2. Chunks are converted into embeddings using Hugging Face models  
3. Embeddings are stored in ChromaDB (vector database)  
4. User queries are embedded and matched via similarity search  
5. Retrieved context is injected into an LLM prompt  
6. LLM generates grounded answers with source attribution  
7. FastAPI exposes the system as a production-ready API  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **LLM Framework:** LangChain  
- **Embeddings & LLMs:** Hugging Face Transformers, Sentence-Transformers, FLAN-T5  
- **Vector Database:** ChromaDB  
- **Backend API:** FastAPI, Uvicorn  
- **Search:** Semantic Vector Search, Multi-Query Expansion  
- **Memory:** In-memory conversational memory  
- **Environment:** Python virtual environment (venv)

---

## 📂 Project Structure

```text
.
├── api/
│   └── main.py              # FastAPI entry point
├── rag/
│   ├── qa_chain.py          # Core RAG pipeline
│   ├── memory.py            # Conversational memory
│   └── prompts.py           # Prompt templates
├── ingestion/
│   └── ingest_docs.py       # Document ingestion & chunking
├── vectorstore/
│   └── chroma_store.py      # ChromaDB setup
├── data/
│   └── HR_Policy_Manual.pdf # Sample documents
├── venv/                    # Virtual environment
├── requirements.txt
└── README.md


⚙️ Setup Instructions

1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/your-username/genai-knowledge-assistant.git
cd genai-knowledge-assistant

2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
Linux / macOS

bash
Copy code
source venv/bin/activate

3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt

📥 Document Ingestion
Place your PDF documents inside the data/ directory and run:

bash
Copy code
python ingestion/ingest_docs.py

This will:

Load documents

Split them into chunks

Generate embeddings

Store them in ChromaDB

▶️ Running the Application
Run FastAPI Backend
bash
Copy code
uvicorn api.main:app --reload
API will be available at:

cpp
Copy code
http://127.0.0.1:8000
API Documentation (Swagger UI)
arduino
Copy code
http://127.0.0.1:8000/docs

🔎 API Endpoints
Health Check
bash
Copy code
GET /health
Response

json
Copy code
{
  "status": "ok"
}
Ask a Question
bash
Copy code
POST /ask
Request

json
Copy code
{
  "question": "What is the casual leave policy?"
}
Response

json
Copy code
{
  "answer": "...",
  "sources": [
    {
      "source": "HR_Policy_Manual.pdf",
      "page": 79
    }
  ]
}

🧠 Conversational Memory
Stores recent user–assistant interactions in memory (RAM)

Enables follow-up questions with contextual understanding

Implemented as a lightweight, session-based buffer

Can be extended to Redis or a database for production use

⚖️ Design Trade-offs
Used open-source local models instead of paid APIs for cost and data privacy

In-memory conversational memory for simplicity

Vector-only search (hybrid search and reranking identified as future improvements)

CPU-based inference (GPU recommended for production)

🔮 Future Enhancements
Hybrid search (BM25 + vector)

Reranking models for improved retrieval precision

Persistent memory (Redis / Database)

Authentication and role-based access

UI layer (Streamlit / React)

GPU-based inference

📌 Use Cases
HR policy assistants

Internal knowledge bases

Employee self-service portals

Enterprise document search

Compliance and audit support tools

📄 License
This project is intended for learning, demonstration, and portfolio purposes.

🙌 Acknowledgements
LangChain

Hugging Face

ChromaDB

FastAPI
