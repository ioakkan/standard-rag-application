from embeddings.base_embedding import BaseEmbedder
from sentence_transformers import SentenceTransformer


# local/self-hosted dense embedding model.
class SentenceTransformerEmbedder(BaseEmbedder):

    def __init__(
     self,
     model_name = "sentence-transformers/all-MiniLM-L6-v2"
    
    ):
     self.model = SentenceTransformer(model_name) 


    def embed_documents(self, texts: list[str]):
        return self.model.encode_document(texts)

    def embed_query(self, text: str):
            print("embed_query input:", text)
            print("embed_query type:", type(text))
            result = self.model.encode(text)
            print("embedding type:", type(result))
            print("embedding shape:", getattr(result, "shape", None))
            return self.model.encode_query(text)


    
 # methods 
        # model.encode(...) -> give text or list[txts] returns  vectors embeddings.shape : (num_texts-chunks, num_dim) (3,384) numpy or tensor
        # model.encode_query(...) -
        # model.encode_document(...)
        # model.similarity(...)

    