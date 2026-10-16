from typing import List, Tuple


def rotate_left(lst: List[int], n: int) -> List[int]:
    n = n % len(lst)
    return lst[n:] + lst[:n]


def normalize_snowflake(lst: List[int]) -> List[int]:
    if type(lst) is not list:
        raise TypeError("'lst' is not of type list")
    n = len(lst)

    # validate input
    if n < 1:
        raise TypeError("'lst' contains less than 1 elementst")

    # trivial case
    if n == 1:
        return lst

    min_val = lst[0]
    min_idx = 0
    for i in range(1, n):
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
        elif lst[i] == min_val:
            old_rotation = rotate_left(lst, min_idx)
            new_rotation = rotate_left(lst, i)
            for j in range(n):
                if new_rotation[j] < old_rotation[j]:
                    min_idx = i
                    break
                elif new_rotation[j] > old_rotation[j]:
                    break
    return rotate_left(lst, min_idx)


def polinomial_module(coeffs: List[int], x: int, mod: int) -> int:
    """
    Evaluate polynomial with given coefficients, base and modulo.

    Note: coefficients are in increasing order, i.e. coeffs[i] is the coefficient for base^i.

    :param coeffs: list of coefficients
    :param base: base of the polynomial
    :param mod: modulo value
    :return: result of polynomial evaluation
    """
    result = 0
    for i, coeff in enumerate(coeffs):
        r = coeff % x * pow(x, i, mod)
        result = (result + r) % mod
    return result


def polinomial(coeffs: List[int], base: int) -> int:
    """
    Evaluate polynomial with given coefficients and base.

    Note: coefficients are in increasing order, i.e. coeffs[i] is the coefficient for base^i.

    :param coeffs: list of coefficients
    :param base: base of the polynomial
    :return: result of polynomial evaluation
    """
    result = 0
    for i, coeff in enumerate(coeffs):
        result += coeff * pow(base, i)
    return result
