from datetime import datetime
from pathlib import Path
from snowflake import Snowflake
from jp_adt import SnowflakeHashSet

SNOWFLAKE_RESULTS = {
    True: "No two snowflakes are alike.",
    False: "Twin snowflakes found.",
}


if __name__ == "__main__":
    # from input read snowflakes filenames
    # foreach filename read snowflakes and check if collection is unique
    # foreach filename print result
    import sys

    if len(sys.argv) < 2:
        print("Usage: python Snowflakes.py <snowflakes_file> [<snowflakes_file> ...]")
        sys.exit(1)

    print("Checking uniqueness of snowflakes in files:")
    print("\n-\t" + "\n-\t".join(sys.argv[1:]))
    print("-.- " * 20)
    print("\nResults:")
    for snowflakes_file in sys.argv[1:]:
        start_time = datetime.now()
        with open(snowflakes_file, "r") as f:
            data = f.readlines()
            snowflakes = [
                Snowflake(list(map(int, line.split()))) for line in data[1:]
            ]  # Skip the first line which contains the number of snowflakes
        snowflake_set = SnowflakeHashSet(snowflakes)
        result = len(snowflake_set) == len(snowflakes)
        end_time = datetime.now()
        print(
            f"{Path(snowflakes_file).name:<46}: {SNOWFLAKE_RESULTS[result]:<32} (Time taken: {end_time - start_time}) [ADT: SnowflakeHashSet]"
        )
    exit(0)
    for snowflakes_file in sys.argv[1:]:
        start_time = datetime.now()
        with open(snowflakes_file, "r") as f:
            data = f.readlines()
            snowflakes = [
                Snowflake(list(map(int, line.split()))) for line in data[1:]
            ]  # Skip the first line which contains the number of snowflakes
        snowflake_set = set(snowflakes)
        result = len(snowflake_set) == len(snowflakes)
        end_time = datetime.now()
        print(
            f"{Path(snowflakes_file).name:<46}: {SNOWFLAKE_RESULTS[result]:<32} (Time taken: {end_time - start_time}) [ADT: set]"
        )
