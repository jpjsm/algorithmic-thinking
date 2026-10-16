import random

from typing import List
from snowflake import Snowflake
from utils import polinomial, rotate_left


def generaterandomsnowflakes(
    rows: int = 10,
) -> List[Snowflake]:

    snowflakes_set = set()
    snowflakes = []
    while len(snowflakes) < rows:
        flake = []
        for _ in range(Snowflake.ARMS):
            flake.append(random.randint(0, Snowflake.ARM_MAX_LENGTH))

        snowflake = Snowflake(flake)
        snowflake_id = polinomial(
            snowflake.normalized.snowflake, Snowflake.ARM_MAX_LENGTH + 1
        )

        if snowflake_id not in snowflakes_set:
            snowflakes_set.add(snowflake_id)
            snowflakes.append(snowflake.normalized)

    return snowflakes


def addduplicates(snowflakes: List[Snowflake], duplicatescount: int) -> List[Snowflake]:
    rowscount = len(snowflakes)
    if rowscount < 1 or duplicatescount < 0:
        raise ValueError("'snowflakes' or 'duplicates' has invalid values")

    # select rows to duplicate
    dups = set()
    while len(dups) < duplicatescount:
        dups.add(random.randint(0, rowscount - 1))

    while dups:
        row_idx = dups.pop()
        snowflake = snowflakes[row_idx]
        snowflake_str = str(snowflake)
        snowflake_arms = list(map(int, snowflake_str.split()))
        dup_snowflake = Snowflake(
            rotate_left(snowflake_arms, random.randint(1, Snowflake.ARMS - 1))
        )
        snowflakes.append(dup_snowflake)

    return snowflakes


if __name__ == "__main__":
    snowflakes = generaterandomsnowflakes(100_000)
    with open("snowflakes_02_100K.txt", "w") as f:
        f.write(f"{len(snowflakes)}\n")
        for snowflake in snowflakes:
            f.write(str(snowflake) + "\n")

    snowflakes = generaterandomsnowflakes(99_999)
    snowflakes = addduplicates(snowflakes, 1)
    with open("snowflakes_02_100K_with_duplicate.txt", "w") as f:
        f.write(f"{len(snowflakes)}\n")
        for snowflake in snowflakes:
            f.write(str(snowflake) + "\n")
