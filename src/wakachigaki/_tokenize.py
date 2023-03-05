from functools import reduce
from typing import List, Tuple

from .feature import featurer
from .model import model
from .predict import predict

n_buckets: int = model["config"]["n_buckets"]  # type: ignore
size: int = model["config"]["size"]  # type: ignore
offset: int = model["config"]["offset"]  # type: ignore


def tokenizer(n_buckets: int, size: int, offset: int):
    f = featurer(n_buckets, size, offset)

    def fn(text: str):
        chars = f(text)
        preds = predict(chars)

        def reducer(acc: List[str], item: Tuple[int, bool]):
            i, will_break = item
            acc[len(acc) - 1] += chars[i].char
            if will_break:
                acc.append("")
            return acc

        x = reduce(reducer, enumerate(preds), [""])
        return list(filter(lambda x: x, x))

    return fn


tokenize = tokenizer(n_buckets, size, offset)

segment = tokenize
