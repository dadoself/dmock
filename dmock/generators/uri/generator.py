from .schemes import schemes
from ..text.generator import generate_ascii_word
import random


class UriGenerationStrategy:
    def generate_scheme(self) -> str:
        raise NotImplementedError()

    def generate_host(self) -> str:
        raise NotImplementedError()


class PureRandomUri(UriGenerationStrategy):
    def generate_scheme(self) -> str:
        return random.choice(schemes)

    def generate_host(self) -> str:
        return generate_ascii_word(3, 4) + "." + generate_ascii_word(5, 6) + "." + generate_ascii_word(2, 3)


class UriGenerator:
    def __init__(self, strategy: UriGenerationStrategy):
        self._strategy = strategy

    def __call__(self, *args, **kwargs):
        uri: str = (self._strategy.generate_scheme() + "://" + self._strategy.generate_host())
        return uri
