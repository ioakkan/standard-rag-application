from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from generation.prompts import rag_prompt
from .base import BaseGenerator


class Generator(BaseGenerator):

    def __init__(self, llm):
        self.llm = llm

    def generate(
        self,
        query: str,
        documents: list[Document],
    ) -> str:

        context = "\n\n".join( # "\n\n" two lines seperator between chunks formatting)
            document.page_content
            for document in documents
        )

        prompt = rag_prompt.format(
        context=context,
        question=query,
        )
        response = self.llm.invoke(prompt)
        return response.content

    def llm_chain(
        self,
        prompt 
    ) -> str:
         
            response = self.llm.invoke(prompt) #return Aimessage?
            return response.content 


