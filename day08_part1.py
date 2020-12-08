# Advent of Code 2020 - Day 8 - Handheld Halting
# https://adventofcode.com/2020/day/8

import sys

def parse_input(lines):
    program = []
    for line in lines:
        instruction, argument = line.strip().split(" ")
        program.append((instruction, int(argument)))
    return program

def run(program):
    pc = 0
    acc = 0
    seen = []
    while pc not in seen and pc < len(program):
        seen.append(pc)
        op, arg = program[pc]
        if op == "acc":
            acc += arg
            pc += 1
        elif op == "jmp":
            pc += arg
        elif op == "nop":
            pc += 1
    return acc, pc
    
def part1(program):
    acc, pc = run(program)
    return acc

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))

