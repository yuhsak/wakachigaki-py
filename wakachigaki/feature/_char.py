from functools import reduce

from ._regexp import (
    is_alphabet,
    is_hiragana,
    is_kanji,
    is_katakana,
    is_numeral,
    is_numeral_kanji,
)

rules = [
    {
        "fn": is_kanji,
        "rep": "C",
    },
    {
        "fn": is_numeral_kanji,
        "rep": "S",
    },
    {
        "fn": is_hiragana,
        "rep": "H",
    },
    {
        "fn": is_katakana,
        "rep": "K",
    },
    {
        "fn": is_alphabet,
        "rep": "A",
    },
    {
        "fn": is_numeral,
        "rep": "N",
    },
]


def get_char_type(char: str):
    return reduce(
        lambda rep, rule: rule["rep"] if rule["fn"](char) else rep, rules, "O"
    )
