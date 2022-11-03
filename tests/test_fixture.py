import random
import pytest


@pytest.fixture()
def ten_elements_list():
    return [random.randint(1, 100) for _ in range(10)]


def test_if_list_len_10(ten_elements_list):
    assert len(ten_elements_list) == 10


def test_if_elements_from_1_to_100(ten_elements_list):
    are_ok = True
    for element in ten_elements_list:
        if element > 100 or element < 1:
            are_ok = False
    assert are_ok

