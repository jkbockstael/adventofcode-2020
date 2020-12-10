# Advent of Code 2020 - Day 9 - Encoding Error - Part 2
# https://adventofcode.com/2020/day/9

import sys
from day09_part1 import parse_input, find_invalid_number

def find_contiguous_set(numbers, target):
    for start in range(0, len(numbers) - 2):
        for stop in range(start, len(numbers) - 1):
            candidates = numbers[start:stop]
            total = sum(candidates)
            if total > target:
                break
            if total == target:
                return candidates

def part2(numbers):
    invalid_number = find_invalid_number(numbers)
    contiguous_set = find_contiguous_set(numbers, invalid_number)
    return min(contiguous_set) + max(contiguous_set)

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

