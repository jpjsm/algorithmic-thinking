from typing import List

from utils import rotate_left

# class MetaSnowflake(type):
#     @property
#     def ARMS(cls) -> int:
#         return 6

#     @property
#     def ARM_MIN_LENGTH(cls) -> int:
#         return 0

#     @property
#     def ARM_MAX_LENGTH(cls) -> int:
#         return 10_000_000

#     @property
#     def HASH_MOD(cls) -> int:
#         return 4_294_967_291


class Snowflake:
    ARMS = 6
    ARM_MIN_LENGTH = 0
    ARM_MAX_LENGTH = 10_000_000
    HASH_MOD = 4_294_967_291

    def __init__(self, flake: List[int]):
        # if type(flake) is not list:
        #     raise TypeError("'flake' is not of type list")
        # if len(flake) != Snowflake.ARMS:
        #     raise ValueError(f"'snowflakes' must contain exactly {Snowflake.ARMS} arms")
        # if not all(
        #     isinstance(arm, int)
        #     and Snowflake.ARM_MIN_LENGTH <= arm <= Snowflake.ARM_MAX_LENGTH
        #     for arm in flake
        # ):
        #     raise TypeError(
        #         f"'snowflakes' must contain only positive integers"
        #         + f" between {Snowflake.ARM_MIN_LENGTH} and {Snowflake.ARM_MAX_LENGTH}"
        #     )

        self.snowflake: List[int] = flake
        self._hash_value: int | None = None  # Cache for the hash value
        self._normalized: List[int] | None = None  # Cache for the normalized snowflake
        self._str_value: str | None = None  # Cache for the string representation

    def __list__(self):
        return self.snowflake

    @property
    def normalized(self) -> List[int]:
        if self._normalized is not None:
            return self._normalized
        current = list(self.snowflake)
        min_val = current[0]
        min_idx = 0
        for i in range(1, Snowflake.ARMS):
            if current[i] < min_val:
                min_val = current[i]
                min_idx = i
            elif current[i] == min_val:
                old_rotation = rotate_left(current, min_idx)
                new_rotation = rotate_left(current, i)
                for j in range(Snowflake.ARMS):
                    if new_rotation[j] < old_rotation[j]:
                        min_idx = i
                        break
                    elif new_rotation[j] > old_rotation[j]:
                        break
        self._normalized = rotate_left(current, min_idx)
        return self._normalized

    def __str__(self):
        if self._str_value is not None:
            return self._str_value
        self._str_value = f"{' '.join(map(str, self.snowflake))}"
        return self._str_value

    def __eq__(self, other):
        if not isinstance(other, Snowflake):
            return False
        me = self.normalized
        alter = other.normalized

        for i in range(Snowflake.ARMS):
            if me[i] != alter[i]:
                return False
        return True

    def __hash__(self):
        if self._hash_value is not None:
            return self._hash_value
        current = self.normalized
        result = 0
        for i, coeff in enumerate(current):
            r = (coeff % Snowflake.HASH_MOD) * pow(
                Snowflake.ARM_MAX_LENGTH, i, Snowflake.HASH_MOD
            )
            result = (result + r) % Snowflake.HASH_MOD
        self._hash_value = result
        return result


if __name__ == "__main__":
    # Example usage
    snowflake1 = Snowflake([2, 3, 4, 5, 6, 1])
    snowflake2 = Snowflake([6, 5, 4, 3, 2, 1])
    snowflake3 = Snowflake([4, 5, 6, 1, 2, 3])
    snowflake4 = Snowflake([2, 3, 4, 5, 6, 1])

    print(f"Snowflake 1: {snowflake1}")
    print(f"Snowflake 2: {snowflake2}")
    print(f"Snowflake 3: {snowflake3}")
    print(f"Snowflake 4: {snowflake4}")

    print(f"Snowflake 1 normalized: {snowflake1.normalized}")
    print(f"Snowflake 2 normalized: {snowflake2.normalized}")
    print(f"Snowflake 3 normalized: {snowflake3.normalized}")
    print(f"Snowflake 4 normalized: {snowflake4.normalized}")

    print(f"Snowflake 1 == Snowflake 2: {snowflake1 == snowflake2}")
    print(f"Snowflake 1 == Snowflake 3: {snowflake1 == snowflake3}")
    print(f"Snowflake 1 == Snowflake 4: {snowflake1 == snowflake4}")

    snowflakes_set = set()
    snowflakes_set.add(snowflake1)
    snowflakes_set.add(snowflake2)
    snowflakes_set.add(snowflake3)
    snowflakes_set.add(snowflake4)

    print(f"Number of unique snowflakes in set: {len(snowflakes_set)}")
    while len(snowflakes_set) > 0:
        flake = snowflakes_set.pop()
        print(f"Unique snowflake: {flake}")
