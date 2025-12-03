import itertools
import re
import math
from solutions.utils import load_input

def part1(data: str) -> int:
    pairs = [tuple(map(int, pair.split("-"))) for pair in data.split(",")]
    res = 0

    for lower, upper in pairs:
        digits = int(math.log10(lower)) + 1

        if digits % 2 == 0:
            first_half = int(str(lower)[:int(digits/2)])
            second_half = int(str(lower)[int(digits/2):])
            curr_subunit = first_half if first_half >= second_half else first_half + 1
        else:
            curr_subunit = 10 ** int(digits / 2)

        for subunit in itertools.count(curr_subunit):
            num = int(str(subunit)+str(subunit))
            if num > upper:
                break
            res += num

    return res

def part2(data: str) -> int:
    pairs = [tuple(map(int, pair.split("-"))) for pair in data.split(",")]
    res = 0
    regex_pattern = re.compile(r"^(\d+?)\1+$")
    for lower, upper in pairs:
        for i in range(lower,upper+1):
            if regex_pattern.search(str(i)):
                res += i
    return res

if __name__ == "__main__":
    data = load_input(2)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")