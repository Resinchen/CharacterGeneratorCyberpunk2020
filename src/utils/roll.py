import random
from enum import Enum
from typing import Callable

RollFunc = Callable[[], int]


def make_roll(n: int) -> RollFunc:
    roll = range(1, n + 1)

    def inner() -> int:
        return random.choice(roll)

    return inner


def is_odd(n: int) -> bool:
    return n % 2 == 0


def is_odd_roll() -> bool:
    return is_odd(roll_10())


def roll_to_type(values: dict[Enum, list[int]]) -> dict[int, Enum]:
    pairs = []
    for k, vl in values.items():
        for v in vl:
            pairs.append((v, k))

    return dict(pairs)


def roll_great(n: int) -> bool:
    return roll_10() > n


roll_10: RollFunc = make_roll(10)
roll_6: RollFunc = make_roll(6)
