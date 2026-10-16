from typing import List, Tuple
from utils import polinomial_module, normalize_snowflake

from snowflake import Snowflake


class SnowflakeHashSet:
    _HI_MOD = 200_003
    _LO_MOD = 127

    def __init__(self, snowflakes: None | List[Snowflake] = None):
        self._set: List[None | List[Tuple[int, List[Snowflake]]]] = [
            None
        ] * SnowflakeHashSet._HI_MOD
        self._len = 0
        self._items: List[Snowflake] = []
        if snowflakes:
            for snowflake in snowflakes:
                if isinstance(snowflake, Snowflake):
                    self.add(snowflake)

    def add(self, snowflake: Snowflake) -> bool:
        if not isinstance(snowflake, Snowflake):
            raise TypeError("'snowflake' is not of type Snowflake")
        hi_hash_value = hash(snowflake) % SnowflakeHashSet._HI_MOD
        lo_hash_value = hash(snowflake) % SnowflakeHashSet._LO_MOD

        if self._set[hi_hash_value] is None:
            self._set[hi_hash_value] = [(lo_hash_value, [snowflake])]
            self._len += 1
            self._items.append(snowflake)
            return True
        for i, (lo_hash, snowflakes) in enumerate(self._set[hi_hash_value]):
            if lo_hash == lo_hash_value:
                if snowflake in snowflakes:
                    return False  # Snowflake already exists
                else:
                    snowflakes.append(snowflake)
                    self._len += 1
                    self._items.append(snowflake)
                    return True
        # If we reach here, it means the lo_hash_vlue was not found
        self._set[hi_hash_value].append((lo_hash_value, [snowflake]))
        self._len += 1
        self._items.append(snowflake)
        return True

    def remove(self, snowflake: Snowflake) -> bool:
        if not isinstance(snowflake, Snowflake):
            raise TypeError("'snowflake' is not of type Snowflake")
        hi_hash_value = hash(snowflake) % SnowflakeHashSet._HI_MOD
        lo_hash_value = hash(snowflake) % SnowflakeHashSet._LO_MOD
        if self._set[hi_hash_value] is None:
            return False  # Snowflake not found
        for i, (lo_hash, snowflakes) in enumerate(self._set[hi_hash_value]):
            if lo_hash == lo_hash_value:
                if snowflake in snowflakes:
                    snowflakes.remove(snowflake)
                    self._len -= 1
                    if not snowflakes:  # If the list is empty, remove the entry
                        del self._set[hi_hash_value][i]
                        if not self._set[
                            hi_hash_value
                        ]:  # If the list is empty, set to None
                            self._set[hi_hash_value] = None
                    return True
                else:
                    return False  # Snowflake not found
        return False

    def contains(self, snowflake: Snowflake) -> bool:
        """
        Check if the snowflake is already in the set.
        """
        if not isinstance(snowflake, Snowflake):
            raise TypeError("'snowflake' is not of type Snowflake")
        hi_hash_value = hash(snowflake) % SnowflakeHashSet._HI_MOD
        lo_hash_value = hash(snowflake) % SnowflakeHashSet._LO_MOD
        if self._set[hi_hash_value] is None:
            return False
        for lo_hash, snowflakes in self._set[hi_hash_value]:
            if lo_hash == lo_hash_value:
                return snowflake in snowflakes
        return False

    def __len__(self):
        return self._len

    def __iter__(self):
        self._iter_index = 0
        return iter(self._items)

    def __next__(self):
        if self._iter_index >= len(self._items):
            raise StopIteration
        snowflake = self._items[self._iter_index]
        self._iter_index += 1
        return snowflake


if __name__ == "__main__":
    # Example usage
    snowflake1 = Snowflake([2, 3, 4, 5, 6, 1])
    snowflake2 = Snowflake([6, 5, 4, 3, 2, 1])
    snowflake3 = Snowflake([4, 5, 6, 1, 2, 3])
    snowflake4 = Snowflake([3, 4, 5, 6, 1, 2])

    snowflake_set = SnowflakeHashSet()
    print(f"Adding snowflake1: {snowflake_set.add(snowflake1)}")
    print(f"Adding snowflake2: {snowflake_set.add(snowflake2)}")
    print(
        f"Adding snowflake3  (duplicate of snowflake1): {snowflake_set.add(snowflake3)}"
    )
    print(
        f"Adding snowflake4 (duplicate of snowflake1): {snowflake_set.add(snowflake4)}"
    )

    print(f"Contains snowflake1: {snowflake_set.contains(snowflake1)}")
    print(f"Contains snowflake3: {snowflake_set.contains(snowflake3)}")
    print(f"Contains snowflake4: {snowflake_set.contains(snowflake4)}")

    for snowflake in snowflake_set:
        print(f"Iterating over snowflake: {snowflake}")

    print(f"Removing snowflake1: {snowflake_set.remove(snowflake1)}")
    print(f"Contains snowflake1 after removal: {snowflake_set.contains(snowflake1)}")
    print(f"Contains snowflake3 after removal: {snowflake_set.contains(snowflake3)}")
    print(f"Contains snowflake4 after removal: {snowflake_set.contains(snowflake4)}")
