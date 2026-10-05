### This is the abstraction shared by all loaders.
from abc import ABC, abstractmethod


class BaseLoader(ABC):

    @abstractmethod
    def load_documents(self, source: str):
        """Load a source and return documents."""
        pass