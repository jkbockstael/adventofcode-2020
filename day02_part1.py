# Advent of Code 2020 - Day 2 - Password Philosophy
# https://adventofcode.com/2020/day/2

import sys

def parse_input(lines):
    return [[field.strip() for field in line.strip().split(":")] for line in lines]

def parse_policy(policy):
    count_range, letter = policy.split(" ")
    count_min, count_max = map(int, count_range.split("-"))
    return (count_min, count_max, letter)

def is_valid(policy, password):
    count_min, count_max, letter = parse_policy(policy)
    return count_min <= password.count(letter) <= count_max

def part1(entries):
    return len([1 for entry in entries if is_valid(entry[0], entry[1])])

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
