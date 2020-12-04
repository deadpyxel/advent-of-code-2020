from typing import Collection

import pytest

from advent_of_code.utils import calc_product


@pytest.mark.fast
@pytest.mark.parametrize(
    ("input_list", "expected"),
    [((), 0), ((2,), 2), ((2, 2), 4), ((5, 3, 4), 60), ((-1, 10), -10)],
)
def test_product_function_returns_correct_result(
    input_list: Collection[int], expected: int
) -> None:
    assert calc_product(input_list) == expected
