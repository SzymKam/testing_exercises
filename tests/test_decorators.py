import pytest
from functionality_code.operations import *


@pytest.mark.power
def test_return_right_value_for_positive_exp():
    base_1 = 10
    base_2 = 7
    exp_1 = 3
    exp_2 = 2
    assert calc_power(base=base_1, exp=exp_1) == 1000
    assert calc_power(base=base_2, exp=exp_2) == 49


@pytest.mark.power
def test_return_1_for_exp_0():
    base_1 = 10
    base_2 = 5
    exp = 0
    assert calc_power(base=base_1, exp=exp) == 1
    assert calc_power(base=base_2, exp=exp) == 1


@pytest.mark.power
def test_return_0_for_base_0():
    base = 0
    exp_1 = 5
    exp_2 = 8
    assert calc_power(base=base, exp=exp_1) == 0
    assert calc_power(base=base, exp=exp_2) == 0


@pytest.mark.power
def test_return_right_value_for_fractional_exp():
    base = 64
    exp = 0.5
    assert calc_power(base=base, exp=exp) == 8


@pytest.mark.power
def test_return_right_value_for_negative_exp():
    base = 10
    exp = -2
    assert calc_power(base=base, exp=exp) == 0.01


@pytest.mark.sequence
def test_return_right_value_for_positive_range():
    start = 1
    end = 10
    assert calc_sum_arith_seq(start=start, end=end) == 55


@pytest.mark.sequence
def test_return_right_value_for_negative_range():
    start = -10
    end = -1
    assert calc_sum_arith_seq(start=start, end=end) == -55


@pytest.mark.sequence
def test_return_right_value_for_1_len_range():
    start = -10
    end = start
    assert calc_sum_arith_seq(start=start, end=end) == start


@pytest.mark.sequence
def test_return_right_value_for_various_range():
    start = -10
    end = 10
    assert calc_sum_arith_seq(start=start, end=end) == 0