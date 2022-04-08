from typing import Sequence


def ngram(chars: Sequence[str]):
    def index(i: int):
        def get(size: int, offset: int) -> str:
            if size == 1:
                return chars[i + offset]
            else:
                return get(size - 1, offset) + get(1, offset + (size - 1))

        return get

    return index
