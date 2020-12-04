import re
from dataclasses import dataclass
from typing import List
from typing import Optional

from advent_of_code.adapter import acquire_problem_input


# TODO: Use proper types and validate on __init__
@dataclass
class ValidPassport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None


def _parse_problem04_input(raw_input: List[str]) -> List[ValidPassport]:
    valid_passports = []
    for passport_data in raw_input:
        data = [d.split("\n") for d in passport_data.split()]
        data_dict = {}
        for d in data:
            k, v = d[0].split(":")
            data_dict[k] = v
        try:
            valid_passports.append(ValidPassport(**data_dict))
        except TypeError:
            continue
    return valid_passports


def validate_range(n: str, lower_limit: int, upper_limit: int) -> bool:
    return n.isnumeric() and lower_limit <= int(n) <= upper_limit


def validate_height(height: str) -> bool:
    return (height.endswith("cm") and validate_range(height[:-2], 150, 193)) or (
        height.endswith("in") and validate_range(height[:-2], 59, 76)
    )


def validate_passport(passport: ValidPassport) -> bool:
    if (
        (
            not validate_range(passport.byr, 1920, 2002)
            or not validate_range(passport.iyr, 2010, 2020)
            or not validate_range(passport.eyr, 2020, 2030)
        )
        or len(passport.pid) != 9
        or passport.ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        or re.match("#[0-9a-f]{6}", passport.hcl) is None
        or not validate_height(passport.hgt)
    ):
        return False
    return True


def validate_part2(current_list: List[ValidPassport]) -> List[ValidPassport]:
    revalidated_passports = []
    for passport in current_list:
        if validate_passport(passport):
            revalidated_passports.append(passport)
    return revalidated_passports


def solve_day04() -> None:
    problem_input = acquire_problem_input(day=4)
    split_input = problem_input.strip().split("\n\n")
    valid_passports = _parse_problem04_input(split_input)

    # Part 1
    print(f"Solution for part1: {len(valid_passports)}")
    # Part 1
    revalidated_passports = validate_part2(valid_passports)
    print(f"Solution for part2: {len(revalidated_passports)}")
