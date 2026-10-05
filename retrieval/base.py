from abc import ABC, abstractmethod
from langchain_core.documents import Document

class BaseRetriever(ABC):

    @abstractmethod
    def retrieve(self, query: str) -> list[Document]:
        pass