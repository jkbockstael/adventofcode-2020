# Advent of Code 2020 - Day 4: Passport Processing - Part 2
# https://adventofcode.com/2020/day/4

import sys
from day04_part1 import parse_input, has_required_keys

def is_number(low, high, value):
    return value.isnumeric() and (low <= int(value) <= high)

def is_height(value):
    return (value.endswith("cm") and is_number(150, 193, value[:-2])) \
        or (value.endswith("in") and is_number(59, 76, value[:-2]))

def is_hex_color(value):
    hex_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", \
        "a", "b", "c", "d", "e", "f"]
    return len(value) == 7 \
        and value[0] == "#" \
        and all(map(lambda x: x in hex_digits, value[1:]))

def is_eye_color(value):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in eye_colors

def is_passport_id(value):
    return len(value) == 9 \
        and all(map(lambda x: x.isdigit(), value))

def is_valid(passport):
    return has_required_keys(passport) \
        and is_number(1920, 2002, passport["byr"]) \
        and is_number(2010, 2020, passport["iyr"]) \
        and is_number(2020, 2030, passport["eyr"]) \
        and is_height(passport["hgt"]) \
        and is_hex_color(passport["hcl"]) \
        and is_eye_color(passport["ecl"]) \
        and is_passport_id(passport["pid"])

def part2(passports):
    return len(list(filter(is_valid, passports)))

if __name__ == "__main__":
    print(part2(parse_input(sys.stdin.readlines())))

