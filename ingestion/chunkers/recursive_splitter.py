from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.chunkers.base_chunker import BaseChunker
from langchain_core.documents import Document


class RecursiveChunker(BaseChunker):

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            #seperators=?
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(self, documents: list[Document]) -> list[Document]:
        return self.splitter.split_documents(documents)