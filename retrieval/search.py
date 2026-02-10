from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_vectorstore(persist_dir="vectorstore/chroma_db"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )

    return vectordb


def similarity_search(query, k=5):
    vectordb = load_vectorstore()
    results = vectordb.similarity_search(query, k=k)
    return results

if __name__ == "__main__":
    query = "What is the leave policy for employees?"
    results = similarity_search(query)

    for i, doc in enumerate(results, 1):
        print(f"\n--- Result {i} ---")
        print(doc.page_content[:500])
        print("Metadata:", doc.metadata)
