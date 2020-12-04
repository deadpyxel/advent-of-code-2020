from typing import Iterable
from typing import List


def parse_input_as_integer(original_input: str) -> List[int]:
    spl = original_input.rstrip().split("\n")
    return [int(i) for i in spl]


def calc_product(input_list: Iterable[int]) -> int:
    result = 1
    for x in input_list:
        result *= x
    return result
