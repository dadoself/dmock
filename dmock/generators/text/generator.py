import string
import random
import itertools


def generate_ascii_word(min_length: int, max_length: int) -> str:
    assert min_length < max_length
    length = random.randrange(min_length, max_length)
    return "".join(map(random.choice, itertools.repeat(string.ascii_letters, length)))
