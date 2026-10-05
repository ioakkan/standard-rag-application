from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from ingestion.chunkers.recursive_splitter import RecursiveChunker
from ingestion.loaders.pdf import PDFLoader
from ingestion.loaders.txt import TXTLoader
from embeddings.sentence_transformer import SentenceTransformerEmbedder
from ingestion.pipeline import IngestionPipeline
from vectorstore.langchain_faiss import FAISSVectorStore


def ingest(
    source: str,
    storage_path: str,
    index_name: str
):
    # Components
    loader = TXTLoader()

    chunker = RecursiveChunker(
        chunk_size=1000,
        chunk_overlap=200
    )

    embeddings_model = SentenceTransformerEmbedder()

    vector_store = FAISSVectorStore(
        embeddings=embeddings_model
    )

    # Pipeline
    pipeline = IngestionPipeline(
        loader=loader,
        chunker=chunker,
        embeddings_model=embeddings_model,
        vector_store=vector_store
    )

    # Run
    pipeline.run(
        source=source,
        storage_path=storage_path,
        index_name=index_name
    )


if __name__ == "__main__":

    ingest(
        source="data/example.txt",
        storage_path="../storage",
        index_name="my_index"
    )
 
# pdf_pipeline = IngestionPipeline(loader, chunker)