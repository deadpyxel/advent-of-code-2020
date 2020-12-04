from typing import List
from typing import Tuple

from advent_of_code.adapter import acquire_problem_input
from advent_of_code.utils import calc_product


def _count_trees(slope: Tuple[int, int], roadmap: List[str]) -> int:
    slope_x, slope_y = slope
    row_len = len(roadmap[0])
    count = 0
    step = 0
    for i, row in enumerate(roadmap[1:], start=1):
        if i % slope_y != 0:
            continue
        step += slope_x
        count += row[step % row_len] == "#"
    return count


def solve_day03():
    problem_input = acquire_problem_input(day=3)
    roadmap = problem_input.strip().split("\n")

    # Part 1 - We were asked to find the amount of trees that will be in a
    # given trajectory, as X steps right, Y steps down
    trees_count = _count_trees(slope=(3, 1), roadmap=roadmap)
    print(f"Solution for part1: {trees_count}")

    # Part 2 - With the same structure of input, we were asked to find the
    # value of the product of trees found by using different slope values
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_per_trajectory = [
        _count_trees(slope=slope, roadmap=roadmap) for slope in slopes
    ]
    trees_count = calc_product(trees_per_trajectory)
    print(f"Solution for part2: {trees_count}")
