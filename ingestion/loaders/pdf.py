# app/ingestion/loaders/pdf.py


from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from .base import BaseLoader


class PDFLoader(BaseLoader) :
   
    def load_documents(self, source: str) -> list[Document]:
      return  PyPDFLoader(source).load()