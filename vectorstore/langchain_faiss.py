from langchain_community.vectorstores import FAISS
from vectorstore.base import BaseVectorStore



class FAISSVectorStore(BaseVectorStore):

    def __init__(
        self,
        embeddings,
        store = None
    ):
        self.embeddings = embeddings
        self.store = store

    # faiss.IndexFlatL2(...) by default its this index flat -> exhaustive search and L2 -euclidean distance
    def create_vector_store(self, documents, embeddings):
        if self.store is None:
            self.store = FAISS.from_documents(
            documents=documents,
            embedding=embeddings,
        
           
            )
           

    def add_documents(self, documents):

        if self.store is None:
            raise RuntimeError(
                "Vector store has not been created"
            )

        return self.store.add_documents(
            documents
        )

  
    def similarity_search(self, query, k=4):
   
        if self.store is None:
            raise RuntimeError(
                "Vector store has not been created"
            )

        results = self.store.similarity_search(
            query=query,
            k=k
        )

        return results

    def max_marginal_relevance_search(self,query):
      
        results = self.vector_store.max_marginal_relevance_search(
            query,
            k=self.k,
        )
        return results

    def save_vector_store(self, folder_path, index_name):

        self.store.save_local(
            folder_path=folder_path,
            index_name= index_name
        )
        
    def load_vector_store(self, folder_path, embeddings, index_name):

        self.store = FAISS.load_local(
            folder_path=folder_path,
            embeddings=embeddings,
            index_name=index_name,
            allow_dangerous_deserialization=True,
        )


# vector store methods
# store.from_documents(...)
# store.from_texts(...)
# store.add_documents(...)
# store.add_texts(...)
# store.similarity_search(...)
# store.similarity_search_with_score(...)
# store.delete(...)
# store.save_local(...)
# store.load_local(...)

