import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]

    split_numbers = re.split(delimiter, numbers)
    return sum(map(int, split_numbers))
