from typing import Iterable
import re


def first(y: Iterable, cond: callable):
    return next(x for x in y if x)


def match_text(text: str) -> callable:
    rx = re.compile(text)
    return lambda s: bool(rx.match(s, re.IGNORECASE))
