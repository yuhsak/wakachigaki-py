from functools import reduce
from typing import Any, Dict, Iterable, List

from ..feature import NgramFeature
from ..model import model, threshold
from ._proba import NgramFeatureWithDistance, proba


def proba_predictor(weight: Dict[str, Any], scale: int):
    p = proba(weight, scale)

    def fn(features: Iterable[NgramFeature], threshold=0.5) -> List[float]:
        def get(acc: Any, feature: NgramFeature):
            f = NgramFeatureWithDistance(
                char=feature.char, features=feature.features, distance=acc["distance"]
            )
            _p = p(f)
            will_break = _p > threshold
            distance = 0 if will_break else acc["distance"] + 1
            return {"value": [*acc["value"], _p], "distance": distance}

        return reduce(get, features, {"value": [], "distance": 0})["value"]  # type: ignore

    return fn


predict_proba = proba_predictor(model["weight"], model["config"]["scale"])  # type: ignore


def predictor(weight: Dict[str, Any], scale: int):
    predict_proba = proba_predictor(weight, scale)

    def fn(features: Iterable[NgramFeature], threshold=threshold):
        return list(map(lambda x: x > threshold, predict_proba(features, threshold)))

    return fn


predict = predictor(model["weight"], model["config"]["scale"])  # type: ignore
