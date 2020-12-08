# Advent of Code 2020 - Day 8 - Handheld Halting - Part 2
# https://adventofcode.com/2020/day/8

import sys
from day08_part1 import parse_input, run

def part2(program):
    for index in range(len(program)):
        op, arg = program[index]
        if op in ["nop", "jmp"]:
            new_program = program[:]
            if op == "nop":
                new_program[index] = ("jmp", arg)
            else:
                new_program[index] = ("nop", arg)
            acc, pc = run(new_program)
            if pc == len(program):
                return acc

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

