from typing import List


def _parse_input_as_integer(original_input: str) -> List[int]:
    spl = original_input.rstrip().split("\n")
    return [int(i) for i in spl]
