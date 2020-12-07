# Advent of Code 2020 - Day 6 - Custom Customs
# https://adventofcode.com/2020/day/6

import sys

def parse_input(lines):
    groups = []
    group = []
    for line in lines:
        if len(line.strip()) == 0:
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
    groups.append(group)
    return groups

def uniques_count(group):
    uniques = set()
    for person in group:
        for answer in person:
            uniques.add(answer)
    return len(uniques)

def part1(groups):
    return sum(uniques_count(group) for group in groups)

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
