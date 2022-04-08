from functools import reduce
from typing import Any, Dict, Iterable, List

from ..feature import NgramFeature, NgramFeatureItem
from ..util import sigmoid


class NgramFeatureWithDistance(NgramFeature):
    distance: int

    def __init__(self, char: str, features: List[NgramFeatureItem], distance: int):
        super().__init__(char, features)
        self.distance = distance


def proba(weight: Dict[str, Any], scale: int):
    bias: float = weight["bias"]

    def f(score: int, item: NgramFeatureItem):
        kind = weight.get(item.kind, {})
        size = kind.get(str(item.size), {})
        offset = size.get(str(item.offset), {})
        value = offset.get(item.value, 0)
        return score + value

    def fn(feature: NgramFeatureWithDistance) -> float:
        features = reduce(f, feature.features, 0)
        distance = feature.distance * weight["distance"]  # type: ignore
        return sigmoid((bias + features + distance) / scale)

    return fn
