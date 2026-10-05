from langchain_openai import ChatOpenAI
 

def create_llm():

    return ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
        
    )

