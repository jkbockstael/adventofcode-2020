# Advent of Code 2020 - Day 5 - Binary Boarding
# https://adventofcode.com/2020/day/5

import sys

def parse_input(lines):
    return [line.strip() for line in lines]

def seat_id(p):
    return int(p
        .replace("F", "0")
        .replace("B", "1")
        .replace("L", "0")
        .replace("R", "1"), 2)

def part1(boarding_passes):
    return max(seat_id(boarding_pass) for boarding_pass in boarding_passes)

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
