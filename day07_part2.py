# Advent of Code 2020 - Day 7 - Handy Haversacks - Part 2
# https://adventofcode.com/2020/day/7

import sys
from day07_part1 import parse_input

def content_count(rules, color):
    count = 1
    for content in rules[color]:
        count += rules[color][content] * content_count(rules, content)
    return count

def part2(rules):
    return content_count(rules, "shiny gold") - 1

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

