# hosted API  #need api key 

from embeddings import base_embedding

from langchain_openai import OpenAIEmbeddings # langchain wrapper for openai embedding model


class OpenAIembeddingModel(base_embedding):

    def __init__(
      self,
      model_name="text-embedding-3-small"
    ):
        self.model =  OpenAIEmbeddings(
        model=model_name
        )

    def embed_documents(self, texts: list[str]):
        self.model.embed_documents(texts)
  
    def embed_query(self, text: str):
        self.model.embed_query(text)