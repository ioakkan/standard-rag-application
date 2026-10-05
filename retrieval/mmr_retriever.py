from .base import BaseRetriever


class MMRRetriever(BaseRetriever):

    def __init__(self, vector_store, k=4):
        self.vector_store = vector_store
        self.k = k

    def retrieve(self, query):
        return self.vector_store.max_marginal_relevance_search(
            query,
            k=self.k,
        )
  
