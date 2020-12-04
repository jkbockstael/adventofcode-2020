# Advent of Code 2020 - Day 3 - Toboggan Trajectory - Part 2
# https://adventofcode.com/2020/day/3

import sys
from operator import mul
from functools import reduce
from day03_part1 import parse_input, count_trees

def part2(trees_map):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    return reduce(
        mul,
        map(lambda s: count_trees(trees_map, s[0], s[1]), slopes))


if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

