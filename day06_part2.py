# Advent of Code 2020 - Day 6 - Custom Customs - Part 2
# https://adventofcode.com/2020/day/6

import sys
from day06_part1 import parse_input
from collections import Counter

def commons_count(group):
    counts = Counter()
    for person in group:
        counts.update(person)
    return len(list(a for a in counts.keys() if counts.get(a) == len(group)))

def part2(groups):
    return sum(commons_count(group) for group in groups)

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

