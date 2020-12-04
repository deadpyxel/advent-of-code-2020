from itertools import combinations
from typing import Collection
from typing import List

from advent_of_code.adapter import acquire_problem_input
from advent_of_code.utils import calc_product
from advent_of_code.utils import parse_input_as_integer


def _filter_possible_combinations(
    original_list: List[int], n: int, combination_size: int = 2
) -> List[Collection[int]]:
    return [
        comb
        for comb in combinations(original_list, r=combination_size)
        if sum(comb) == n
    ]


def solve_day01() -> None:
    problem_input = acquire_problem_input()
    input_as_integers = parse_input_as_integer(problem_input)

    # Part 1 - We were asked to find product of a pair from the input
    # that has a sum of 2020
    possible_values = _filter_possible_combinations(input_as_integers, n=2020)
    for possibility in possible_values:
        print(f"Possible answer for part1: {calc_product(possibility)}")

    # Part 2 - We were asked the prompt, but now with a triplet
    possible_values = _filter_possible_combinations(
        input_as_integers, n=2020, combination_size=3
    )
    for possibility in possible_values:
        print(f"Possible answer for part2: {calc_product(possibility)}")
