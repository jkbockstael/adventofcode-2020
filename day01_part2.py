# Advent of Code 2020 - Day 1 - Report Repair - Part 2
# https://adventofcode.com/2020/day/1

import sys
from day01_part1 import parse_input

def part2(expenses):
    return [a * b * c 
        for a in expenses
        for b in expenses
        for c in expenses
        if a + b + c == 2020][0]

print(part2(parse_input(sys.stdin.readlines())))
