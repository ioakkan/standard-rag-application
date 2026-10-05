from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

def create_rag_chain(retriever, prompt, llm):
    retriever_runnable =  RunnableLambda(retriever.retrieve)
    llm_runnable = RunnableLambda(llm.llm_chain)
    rag_chain = (
        {
            "context": retriever_runnable,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm_runnable
        #StrOutParser
    )

    return rag_chain