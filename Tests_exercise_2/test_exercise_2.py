from Tests_exercise_2.exercise_2 import fizz_buzz
import pytest


class TestFizzBuzz:
    @pytest.mark.parametrize('number', [3, 6, 33, ])
    def test_if_number_divisible_by_3_return_fizz(self, number):
        expected = 'fizz'
        assert fizz_buzz(number=number) == expected

    @pytest.mark.parametrize('number', [5, 10, 25, 20])
    def test_if_number_divisible_by_5_return_buzz(self, number):
        expected = 'buzz'
        assert fizz_buzz(number=number) == expected

    @pytest.mark.parametrize('number', [15, 90, 360, 30])
    def test_if_number_divisible_by_5_and_3_return_fizz_buzz(self, number):
        expected = 'fizzbuzz'
        assert fizz_buzz(number=number) == expected

    def test_if_number_0_return_0(self):
        number = 0
        expected = 0
        assert fizz_buzz(number=number) == expected

    @pytest.mark.parametrize('number', [13, 19, 37, 17])
    def test_if_positive_number_return_nothing(self, number):
        expected = 0
        assert fizz_buzz(number=number) == expected

    @pytest.mark.parametrize('number', [-13, -17, -37, -19])
    def test_if_negative_number_return_nothing(self, number):
        expected = 0
        assert fizz_buzz(number=number) == expected
