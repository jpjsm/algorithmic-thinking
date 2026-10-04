from typing import List, Tuple


def rotate_left(lst: List[int], n: int) -> List[int]:
    n = n % len(lst)
    return lst[n:] + lst[:n]


def normalize_snowflake(lst: List[int]) -> Tuple[int, ...]:
    n = len(lst)

    # validate input
    if n < 1:
        raise TypeError("'lst' contains less than 1 elements or is not of type list")

    # trivial case
    if n == 1:
        return tuple(lst)

    # find first smallest item in the list
    lowest, idx = (lst[0], 0)

    for i in range(1, n):
        if lst[i] < lowest:
            lowest, idx = (lst[i], i)

    return tuple(lst[idx:] + lst[:idx]) if idx > 0 else tuple(lst)
