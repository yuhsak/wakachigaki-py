import math


def sigmoid(v: float):
    return 1 / (1 + math.e ** (-1 * v))
