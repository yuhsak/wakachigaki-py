import re

regexp = {
    "Kanji": re.compile(
        r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F][\uDC00-\uDFFF]"
    ),
    "NumeralKanji": re.compile(r"[一二三四五六七八九十百千万億兆]"),
    "Hiragana": re.compile(r"[ぁ-ん]"),
    "Katakana": re.compile(r"[ァ-ヴーｧ-ﾝﾞﾟ]"),
    "Alphabet": re.compile(r"[a-zA-Zａ-ｚＡ-Ｚ]"),
    "Numeral": re.compile(r"[0-9０-９]"),
}


def is_kanji(text: str):
    return bool(regexp["Kanji"].match(text))


def is_numeral_kanji(text: str):
    return bool(regexp["NumeralKanji"].match(text))


def is_hiragana(text: str):
    return bool(regexp["Hiragana"].match(text))


def is_katakana(text: str):
    return bool(regexp["Katakana"].match(text))


def is_alphabet(text: str):
    return bool(regexp["Alphabet"].match(text))


def is_numeral(text: str):
    return bool(regexp["Numeral"].match(text))
