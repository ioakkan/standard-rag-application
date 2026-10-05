from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from generation.prompts import rag_prompt


class RAGApplication():

    def __init__(
        self,
        ingestion_pipeline,
        rag_chain,
    ):
        self.ingestion_pipeline = ingestion_pipeline
        self.rag_chain = rag_chain

    def index(self, source: str,storage_path: str, index_name: str) -> None:
        self.ingestion_pipeline.run (
        source=source,
        storage_path=storage_path,
        index_name=index_name
    )

    def query(self, question: str) -> str:
        return self.rag_chain.invoke(question)





