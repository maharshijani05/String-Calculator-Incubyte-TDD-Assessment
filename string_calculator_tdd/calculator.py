import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]

    nums = list(map(int, re.split(delimiter, numbers)))
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise Exception("negative numbers not allowed " + ",".join(map(str, negatives)))
    return sum(nums)
