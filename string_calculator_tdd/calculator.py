import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter_line = parts[0][2:]
        numbers = parts[1]

        if delimiter_line.startswith("["):
            delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
            delimiter = "|".join(map(re.escape, delimiters))
        else:
            delimiter = re.escape(delimiter_line)
    else:
        if numbers.find("*") > 0:
            length = numbers.count("*") + 1
            newNums = numbers.split("*")
            ans = 1
            for i in range(length):
                ans = ans*int(newNums[i][0])
            return ans

    nums = [int(n) for n in re.split(delimiter, numbers) if n != '']

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise Exception("negative numbers not allowed " + ",".join(map(str, negatives)))
    
    nums = [n for n in nums if n <= 1000]

    return sum(nums)
