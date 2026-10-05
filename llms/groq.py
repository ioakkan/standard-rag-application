from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

def create_groq_llm():
    return ChatGroq(
        model="openai/gpt-oss-20b", 
        temperature=0,
    )