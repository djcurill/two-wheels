from typing import Iterable
import re


def first(y: Iterable, cond: callable):
    return next(x for x in y if x)


def match_text(text: str) -> callable:
    rx = re.compile(text)
    return lambda s: bool(rx.match(s, re.IGNORECASE))


def to_dict(items: list[tuple]) -> dict:
    return {key: val for (key, val) in items}
