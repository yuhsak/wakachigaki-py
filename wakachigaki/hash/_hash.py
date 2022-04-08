from ._crc32 import crc32


def str_to_hash(n_buckets: int):
    def fn(text: str):
        return hex(crc32(text.encode("utf-8")) % n_buckets)[2:].lower()

    return fn
