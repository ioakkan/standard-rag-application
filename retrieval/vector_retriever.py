from .base import BaseRetriever


class VectorRetriever(BaseRetriever):

    def __init__(self, vector_store, k=4):
        self.vector_store = vector_store
        self.k = k

    def retrieve(self, query):
        return self.vector_store.similarity_search(
            query,
            k=self.k,
        )