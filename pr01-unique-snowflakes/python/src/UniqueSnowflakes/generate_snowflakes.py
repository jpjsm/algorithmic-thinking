import random

from utils import rotate_left, normalize_snowflake
from typing import List, Tuple


def generatesnowflakes(
    rows: int = 10, sides: int = 6, int_range: int = 10
) -> List[List[int]]:
    snowflakes = []
    for _ in range(rows):
        snowflake = []
        for _ in range(sides):
            snowflake.append(random.randint(0, int_range))
        snowflakes.append(snowflake)
    return snowflakes


def addduplicates(snowflakes: List[List[int]], duplicatescount: int) -> List[List[int]]:
    rowscount = len(snowflakes)
    if rowscount < 1 or duplicatescount < 0:
        raise ValueError("'snowflakes' or 'duplicates' has invalid values")

    # select rows to duplicate
    dups = set()
    while len(dups) < duplicatescount:
        dups.add(random.randint(0, rowscount))

    while dups:
        row_idx = dups.pop()
        new_row = list(snowflakes[row_idx])
        snowflakes.append(rotate_left(new_row, random.randint(1, len(new_row) - 1)))

    return snowflakes


if __name__ == "__main__":
    snowflakes = generatesnowflakes()
    snowflakes = addduplicates(snowflakes, 1)

    for snowflake in sorted(snowflakes):
        print(snowflake)

    normalized_snowflakes = []
    for snowflake in snowflakes:
        normalized_snowflakes.append(normalize_snowflake(snowflake))

    for normalized_snowflake in sorted(normalized_snowflakes):
        print(normalized_snowflake)
