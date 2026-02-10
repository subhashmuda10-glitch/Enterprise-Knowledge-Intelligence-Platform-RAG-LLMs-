from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from rag.memory import ConversationMemory
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


memory = ConversationMemory(max_turns=3)

def load_vectorstore(persist_dir="vectorstore/chroma_db"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )

def generate_queries(question):
    base_queries = [
        question,
        f"rules for {question}",
        f"HR policy related to {question}",
        f"conditions for {question}",
        f"eligibility criteria for {question}",
    ]

    # remove duplicates
    unique_queries = list(dict.fromkeys(base_queries))
    return unique_queries



def load_llm():
    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256
    )
    return HuggingFacePipeline(pipeline=pipe)


def ask_question(question, k=3):
    vectordb = load_vectorstore()
    llm = load_llm()

    expanded_queries = generate_queries(question)

    all_docs = []
    for q in expanded_queries:
        docs = vectordb.similarity_search(q, k=k)
        all_docs.extend(docs)

    unique_docs = {
        doc.page_content: doc for doc in all_docs
    }.values()

    context = "\n\n".join(
        [doc.page_content for doc in list(unique_docs)[:k]]
    )

    conversation_context = memory.get_context()

    prompt = f"""
        You are an enterprise HR assistant.

        Conversation so far:
        {conversation_context}

        Using ONLY the context below:
        - Answer clearly and concisely
        - Summarize in simple language
        - Do NOT copy text verbatim
        - If the answer is not present, say "I don't know"

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

    answer = llm.invoke(prompt)

    # save to memory
    memory.add(question, answer)

    return answer, list(unique_docs)



if __name__ == "__main__":
    q1 = "What is the casual leave policy?"
    a1, _ = ask_question(q1)
    print("\nQ1:", q1)
    print("A1:", a1)

    q2 = "What about half-day?"
    a2, _ = ask_question(q2)
    print("\nQ2:", q2)
    print("A2:", a2)

