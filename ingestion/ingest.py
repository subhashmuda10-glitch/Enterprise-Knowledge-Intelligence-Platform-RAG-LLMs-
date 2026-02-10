from ingestion.loaders import load_documents
from ingestion.chunking import chunk_documents
from vectorstore.chroma_store import create_chroma_store

docs = load_documents()
chunks = chunk_documents(docs)

print(f"Documents loaded: {len(docs)}")
print(f"Chunks created: {len(chunks)}")

vectordb = create_chroma_store(chunks)
print("ChromaDB vector store created and persisted")
