from abc import ABC, abstractmethod
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

class BaseVectorStore(ABC):
    def __init__(self, embeddings):
        self.embeddings = embeddings

    @abstractmethod
    def add_documents(
        self,
        documents: list[Document],
    ) -> list[str]:
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ) -> list[Document]:
        pass
    @abstractmethod
    def create_vector_store(
        self,
        documents : list[Document],
        embeddings
    ) -> None:
        pass
    @abstractmethod
    def save_vector_store(self, folder_path:str):
                pass
        
    @abstractmethod
    def load_vector_store(self, folder_path:str, embeddings):

        pass
        
# class BaseVectorStore:
#     def add_documents(...)
#     def add_embeddings(...)
#     def similarity_search(...)
#     def similarity_search_by_vector(...)
#     def get_by_ids(...)
#     def delete(...)

