from typing import Collection
from typing import List


def parse_input_as_integer(original_input: str) -> List[int]:
    spl = original_input.rstrip().split("\n")
    return [int(i) for i in spl]


def calc_product(input_list: Collection[int]) -> int:
    if len(input_list) == 0:
        return 0
    result = 1
    for x in input_list:
        result *= x
    return result
