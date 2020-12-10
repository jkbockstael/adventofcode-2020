# Advent of Code 2020 - Day 9 - Encoding Error
# https://adventofcode.com/2020/day/9

import sys

def parse_input(lines):
    return [int(line) for line in lines]

def sum_of_two(preamble, number):
    candidates = [(a,b) for a in preamble for b in preamble if a + b == number]
    return len(candidates) > 0

def find_invalid_number(numbers):
    PREAMBLE_SIZE = 25
    for index in range(PREAMBLE_SIZE, len(numbers)):
        number = numbers[index]
        preamble = numbers[index - PREAMBLE_SIZE:index]
        if not sum_of_two(preamble, number):
            return number

def part1(numbers):
    return find_invalid_number(numbers)
    

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
