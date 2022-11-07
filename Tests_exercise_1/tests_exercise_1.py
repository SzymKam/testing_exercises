from Tests_exercise_1.exercise_1 import number_is_prime
import pytest


class TestIsPrime:
    @pytest.mark.parametrize('test_number, expected_result', [(-5, False), (0, False), (1, False)])
    def test_if_negative_is_prime_return_false(self, test_number, expected_result):
        assert number_is_prime(test_number) == expected_result

    @pytest.mark.parametrize('test_number, expected_result', [(5, True), (13, True)])
    def test_if_positive_passed_number_return_true(self, test_number, expected_result):
        assert number_is_prime(test_number) == expected_result

