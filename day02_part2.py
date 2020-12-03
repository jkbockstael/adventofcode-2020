# Advent of Code 2020 - Day 2 - Password Philosophy - Part 2
# https://adventofcode.com/2020/day/2

import sys
from day02_part1 import parse_input, parse_policy

def xor(p1, p2):
    return (p1 or p2) and not (p1 and p2)

def is_valid(policy, password):
    a, b, letter = parse_policy(policy)
    return xor(password[a - 1] == letter, password[b - 1] == letter)

def part2(entries):
    return len([1 for entry in entries if is_valid(entry[0], entry[1])])

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))
