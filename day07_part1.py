# Advent of Code 2020 - Day 7 - Handy Haversacks
# https://adventofcode.com/2020/day/7

import sys

def parse_input(lines):
    """
    the rule
    "light red bags contain 1 bright white bag, 2 muted yellow bags."
    is parsed into
    {'light red': {'bright white': 1, 'muted yellow': 2}
    """
    rules = dict()
    for line in lines:
        holder_color, content_raw = line.split(" bags contain ")
        rules[holder_color] = dict()
        content_rules = content_raw.split(",")
        for content_rule in content_rules:
            if "no other bag" not in content_rule:
                count, adjective, color, _ = content_rule.strip().split(" ")
                rules[holder_color][adjective + " " + color] = int(count)
    return rules

def can_contain(rules, container, color):
    if color in rules[container]:
        return True
    else:
        return any([can_contain(rules, content, color) \
            for content in rules[container]])

def possible_parents(rules, color):
    return [container for container in rules \
        if can_contain(rules, container, color)]

def part1(rules):
    return len(possible_parents(rules, "shiny gold"))

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
