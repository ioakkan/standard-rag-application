from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        """Send a prompt to the model and return generated text."""
        pass