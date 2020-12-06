# Advent of Code 2020 - Day 4 - Passport Processing
# https://adventofcode.com/2020/day/4

import sys

def parse_input(lines):
    passports = []
    passport = {}
    for line in lines:
        if len(line.strip()) == 0:
            passports.append(passport)
            passport = {}
        else:
            pairs = line.split(" ")
            for pair in pairs:
                key, value = pair.split(":")
                passport[key] = value.strip()
    passports.append(passport)
    return passports

def has_required_keys(passport):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in passport.keys():
            return False
    return True

def part1(passports):
    return len(list(filter(has_required_keys, passports)))

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
