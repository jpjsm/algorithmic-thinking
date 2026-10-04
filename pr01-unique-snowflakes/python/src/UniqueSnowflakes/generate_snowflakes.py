import random

from utils import rotate_left, normalize_snowflake
from typing import List, Tuple


def generaterandomsnowflakes(
    rows: int = 10, sides: int = 6, int_range: int = 10
) -> List[List[int]]:
    snowflakes_normalized = set()
    snowflakes = []
    while len(snowflakes) < rows:
        snowflake = []
        for _ in range(sides):
            snowflake.append(random.randint(0, int_range))

        snowflake_normalized = normalize_snowflake(snowflake)
        if snowflake_normalized not in snowflakes_normalized:
            snowflakes.append(snowflake)
            snowflakes_normalized.add(snowflake_normalized)

    return snowflakes


def addduplicates(snowflakes: List[List[int]], duplicatescount: int) -> List[List[int]]:
    rowscount = len(snowflakes)
    if rowscount < 1 or duplicatescount < 0:
        raise ValueError("'snowflakes' or 'duplicates' has invalid values")

    # select rows to duplicate
    dups = set()
    while len(dups) < duplicatescount:
        dups.add(random.randint(0, rowscount - 1))

    while dups:
        row_idx = dups.pop()
        new_row = list(snowflakes[row_idx])
        snowflakes.append(rotate_left(new_row, random.randint(1, len(new_row) - 1)))

    return snowflakes


if __name__ == "__main__":
    snowflakes = generaterandomsnowflakes()
    snowflakes = addduplicates(snowflakes, 1)

    triplets = []
    for i, snowflake in enumerate(sorted(snowflakes)):
        triplets.append((i, snowflake, normalize_snowflake(snowflake)))

    for t in sorted(triplets, key=lambda t: t[2]):
        print(t[2], t[0], t[1])
