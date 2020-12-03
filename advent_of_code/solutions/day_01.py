from typing import List, Sequence
from itertools import combinations

from advent_of_code.adapter import acquire_problem_input
from advent_of_code.utils import _parse_input_as_integer


def filter_possible_combinations(
    original_list: List[int], n: int, size: int = 2
) -> List[Sequence[int]]:
    return [pair for pair in combinations(original_list, r=size) if sum(pair) == n]


def calc_product(input_list: Sequence[int]) -> int:
    result = 1
    for x in input_list:
        result *= x
    return result


def solve_day01() -> None:
    problem_input = acquire_problem_input()
    input_as_integers = _parse_input_as_integer(problem_input)

    # Part 1 - We were asked to find product of a pair from the input
    # that has a sum of 2020
    possible_values = filter_possible_combinations(input_as_integers, n=2020)
    for possibility in possible_values:
        print(f"Possible answer for part1: {calc_product(possibility)}")

    # Part 2 - We were asked the prompt, but now with a triplet
    possible_values = filter_possible_combinations(input_as_integers, n=2020, size=3)
    for possibility in possible_values:
        print(f"Possible answer for part2: {calc_product(possibility)}")