from functionality_code.operations import *


def test_return_right_value_for_positive_range():
    start = 1
    end = 10
    assert calc_sum_arith_seq(start=start, end=end) == 55


def test_return_right_value_for_negative_range():
    start = -10
    end = -1
    assert calc_sum_arith_seq(start=start, end=end) == -55


def test_return_right_value_for_1_len_range():
    start = -10
    end = start
    assert calc_sum_arith_seq(start=start, end=end) == start


def test_return_right_value_for_various_range():
    start = -10
    end = 10
    assert calc_sum_arith_seq(start=start, end=end) == 0
