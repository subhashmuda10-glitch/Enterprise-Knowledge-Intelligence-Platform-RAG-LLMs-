import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

def load_documents(data_dir="data"):
    documents = []

    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)

        if filename.lower().endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

        elif filename.lower().endswith(".docx"):
            loader = Docx2txtLoader(file_path)
            documents.extend(loader.load())

    return documents
