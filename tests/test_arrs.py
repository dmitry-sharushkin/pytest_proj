from utils.arrs import get
from utils.arrs import my_slice


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([1, 2], -1, "test") == "test"


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert my_slice([1, 2, 3, 4, 5], -2) == [4, 5]
    assert my_slice([]) == []
    assert my_slice([1, 2, 3, 4, 5], 10) == []
    assert my_slice([1, 2, 3, 4, 5], -10) == [1, 2, 3, 4, 5]

