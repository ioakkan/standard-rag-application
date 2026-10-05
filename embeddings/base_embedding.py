from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings

class BaseEmbedder(Embeddings):

    @abstractmethod
    def embed_documents(self, texts: list[str]):
        pass

    @abstractmethod
    def embed_query(self, text: str):
        pass