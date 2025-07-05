import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    split_numbers = re.split(",|\n", numbers)
    return sum(map(int, split_numbers))