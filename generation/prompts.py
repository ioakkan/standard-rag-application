from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template("""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}
""")

