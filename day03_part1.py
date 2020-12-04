# Advent of Code 2020 - Day 3 - Toboggan Trajectory
# https://adventofcode.com/2020/day/3

import sys

def parse_input(lines):
    return [[char for char in line.strip()] for line in lines]

def count_trees(trees_map, slope_col, slope_row):
    row = 0
    col = 0
    trees = 0
    height = len(trees_map)
    width = len(trees_map[0])
    while row < height - 1:
        row = row + slope_row
        col = (col + slope_col) % width
        if trees_map[row][col] == "#":
            trees += 1
    return trees

def part1(trees_map):
    return count_trees(trees_map, 3, 1)

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
