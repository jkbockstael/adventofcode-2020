# Advent of Code 2020 - Day 1 - Report Repair
# https://adventofcode.com/2020/day/1

import sys

def parse_input(lines):
    return [int(line.strip()) for line in lines]

def part1(expenses):
    return [a * b for a in expenses for b in expenses if a + b == 2020][0]

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
