from typing import Any
from typing import Dict
from typing import List

from advent_of_code.adapter import acquire_problem_input


def _parse_problem2_input(
    raw_input: str,
) -> List[Dict[str, Any]]:
    input_list = raw_input.rstrip().split("\n")
    processed_input = []
    for item in input_list:
        criteria: str
        password: str
        criteria, password = item.split(":")
        password = password[1:]
        target_qty, target_letter = criteria.split()
        lower_limit, upper_limit = map(int, target_qty.split("-"))
        processed_input.append(
            {
                "password": password,
                "letter": target_letter,
                "criteria": (lower_limit, upper_limit),
            }
        )
    return processed_input


def _find_valid_password_part1(password_list: List[Dict[str, Any]]) -> List[str]:
    return [
        it["password"]
        for it in password_list
        if it["criteria"][0] <= it["password"].count(it["letter"]) <= it["criteria"][1]
    ]


def _find_valid_password_part2(password_list: List[Dict[str, Any]]) -> List[str]:
    valid_passwords = []
    for password in password_list:
        current_password = password["password"]
        desired_letter = password["letter"]
        # the input does not follow a 0-index rule so we convert
        pos1, pos2 = map(lambda x: x - 1, password["criteria"])
        # only either positions are valid, so we use XOR
        if (current_password[pos1] == desired_letter) ^ (
            current_password[pos2] == desired_letter
        ):
            valid_passwords.append(current_password)
    return valid_passwords


def solve_day02() -> None:
    problem_input = acquire_problem_input(day=2)
    processed_input = _parse_problem2_input(problem_input)

    # Part 1 - We were asked to find how many valid passwords exist in the input
    # given the criteria for the passwords (given letter appers [a-b] times )
    valid_passwords = _find_valid_password_part1(processed_input)
    print(f"Solution for part1: {len(valid_passwords)}")

    # Part 2 - We were asked to find how many valid passwords exist in the input
    # given the criteria for the passwords (letter appears in positions a and b )
    valid_passwords = _find_valid_password_part2(processed_input)
    print(f"Solution for part2: {len(valid_passwords)}")
