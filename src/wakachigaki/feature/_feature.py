from functools import reduce
from typing import List, Tuple

from ..hash import str_to_hash
from ..model import model
from ..util import ngram, normalize
from ._char import get_char_type

markers = [
    "B",
    "D",
    "E",
    "F",
    "G",
    "I",
    "J",
    "L",
    "M",
    "P",
    "Q",
    "R",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


class NgramFeatureItem:
    kind: str
    size: int
    offset: int
    value: str

    def __init__(self, kind: str, size: int, offset: int, value: str):
        self.kind = kind
        self.size = size
        self.offset = offset
        self.value = value


class NgramFeature:
    char: str
    features: List[NgramFeatureItem]

    def __init__(self, char: str, features: List[NgramFeatureItem]):
        self.char = char
        self.features = features


def featurer(n_buckets: int, size: int, offset: int):

    prefix = markers[:offset]
    suffix = list(reversed(markers))[:offset]
    h = str_to_hash(n_buckets)

    def fn(text: str):
        source = normalize(text)
        chars = list(source)

        ngram_by_chars = ngram(prefix + list(source.lower()) + suffix)
        ngram_by_types = ngram(prefix + list(map(get_char_type, chars)) + suffix)

        def get(item: Tuple[int, str]):
            i, char = item
            index = i + offset
            ngram_by_chars_at = ngram_by_chars(index)
            ngram_by_types_at = ngram_by_types(index)

            def get_size(acc: NgramFeature, s: int):
                def get_offset(acc: NgramFeature, o: int):
                    _t = ngram_by_types_at(s, o)
                    _h = h(ngram_by_chars_at(s, o))
                    return NgramFeature(
                        char=acc.char,
                        features=[
                            *acc.features,
                            NgramFeatureItem(kind="type", size=s, offset=o, value=_t),
                            NgramFeatureItem(kind="hash", size=s, offset=o, value=_h),
                        ],
                    )

                return reduce(get_offset, range(-1 * offset, offset + 1 + 1 - s), acc)

            return reduce(
                get_size, range(1, size + 1), NgramFeature(char=char, features=[])
            )

        return list(map(get, enumerate(chars)))

    return fn


config = model["config"]

features = featurer(config["n_buckets"], config["size"], config["offset"])  # type: ignore
