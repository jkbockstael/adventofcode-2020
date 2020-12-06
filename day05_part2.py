# Advent of Code 2020 - Day 5 - Binary Boarding - Part 2
# https://adventofcode.com/2020/day/5

import sys
from day05_part1 import parse_input, seat_id

def part2(boarding_passes):
    seat_ids = [seat_id(boarding_pass) for boarding_pass in boarding_passes]
    free_seats = [seat_id \
        for seat_id in range(min(seat_ids), max(seat_ids)) \
        if seat_id not in seat_ids]
    return free_seats[0]

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

