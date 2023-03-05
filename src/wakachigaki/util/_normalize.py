import unicodedata


def normalize(text: str):
    return unicodedata.normalize("NFC", text).encode("utf-8", "ignore").decode("utf-8")
