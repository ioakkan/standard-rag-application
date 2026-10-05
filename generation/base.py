from abc import ABC, abstractmethod
from langchain_core.documents import Document


class BaseGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        query: str,
        documents: list[Document],
    ) -> str:
        pass
    
    @abstractmethod
    def llm_chain(
        self,
        prompt
    ) -> str:
        pass