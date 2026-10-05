from .base import BaseLoader

from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain_core.documents import Document
from pathlib import Path


class TXTLoader(BaseLoader):

    def load_documents(self, source: str) -> list[Document]:
        path = Path(source)

        # Case 1: source is one .txt file
        if path.is_file():

            if path.suffix.lower() != ".txt":
                raise ValueError(f"Expected a .txt file, got: {path}")

            return TextLoader(
                str(path),
                encoding="utf-8"
            ).load()

        # Case 2: source is a directory
        elif path.is_dir():

            return DirectoryLoader(
                str(path),
                glob="**/*.txt",
                loader_cls=TextLoader,
                loader_kwargs={"encoding": "utf-8"},
            ).load()

        # Case 3: source doesn't exist
        else:
            raise FileNotFoundError(
                f"Could not find file or directory: {source}"
            )