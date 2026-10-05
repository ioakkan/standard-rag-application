
from pathlib import Path
import sys
# # Add rag_pipeline/ to Python's import path
# PROJECT_ROOT = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(PROJECT_ROOT))

from vectorstore.langchain_faiss import FAISSVectorStore


class IngestionPipeline:
    def __init__(
      self,
      loader, 
      chunker,
      embeddings_model,
      vector_store
    
    ):
      self.loader = loader
      self.chunker = chunker
      self.embeddings_model = embeddings_model
      self.vector_store = vector_store
      


    def run(self,source,storage_path,index_name):
 
      documents = self.loader.load_documents(source)  
      chunks = self.chunker.split_documents(documents) 
      storage_path =  Path(storage_path)
      index_boolean = (storage_path / f"{index_name}.faiss").exists() # fix the extension for universal vectorstores

      if index_boolean:

        print(f"Loading existing vector store from {storage_path}...")
        self.vector_store.load_vector_store(storage_path,self.embeddings_model,index_name)
        print(f"Existing index: {index_name} was loaded")

       
        self.vector_store.add_documents(chunks)
        self.vector_store.save_vector_store(storage_path,index_name)
        print("FAISS index updated and saved!")

      else:
       
        storage_path.mkdir(parents=True, exist_ok=True)
        print("Creating a new vector store...")
       
        self.vector_store.create_vector_store(chunks, self.embeddings_model) 
        self.vector_store.save_vector_store(storage_path,index_name=index_name)
        print("New vector store created and saved!")

       