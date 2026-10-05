
from embeddings.sentence_transformer import SentenceTransformerEmbedder
from ingestion.loaders.txt import TXTLoader
from ingestion.chunkers.recursive_splitter import  RecursiveChunker
from vectorstore.langchain_faiss import FAISSVectorStore
from retrieval.vector_retriever import VectorRetriever
from ingestion.pipeline import IngestionPipeline
from .chain import create_rag_chain
from .rag_application import RAGApplication
from generation.generator import Generator
from generation.prompts import rag_prompt
from llms.groq import create_groq_llm

def create_rag_application():

    loader = TXTLoader()

    chunker =  RecursiveChunker(
        chunk_size=1000,
        chunk_overlap=200,
    )

    embeddings = SentenceTransformerEmbedder()

    vector_store = FAISSVectorStore(
        embeddings=embeddings
    )

    retriever = VectorRetriever(
        vector_store=vector_store,
        k=4,
    )

    llm = create_groq_llm()

    generator = Generator(llm)
    
    prompt = rag_prompt

    rag_chain = create_rag_chain(
        retriever=retriever,
        prompt=prompt,
        llm=generator,
    )

    ingestion_pipeline = IngestionPipeline(
        loader=loader,
        chunker=chunker,
        embeddings_model=embeddings,
        vector_store=vector_store,

    )

    return RAGApplication(
        ingestion_pipeline=ingestion_pipeline,
        rag_chain=rag_chain,
    )