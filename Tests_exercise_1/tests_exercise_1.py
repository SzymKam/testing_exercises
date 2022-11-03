import Tests_exercise_1.exercise_1


class TestIsPrime:
    def test_if_negative_is_prime_return_false(self):
        test_number = -5
        expected_result = False
        assert Tests_exercise_1.exercise_1.number_is_prime(test_number) == expected_result

    def test_if_zero_is_prime_return_false(self):
        test_number = 0
        expected_result = False
        assert Tests_exercise_1.exercise_1.number_is_prime(test_number) == expected_result

    def test_if_one_is_prime_return_false(self):
        test_number = 1
        expected_result = False
        assert Tests_exercise_1.exercise_1.number_is_prime(test_number) == expected_result

    def test_if_five_is_prime_return_true(self):
        test_number = 5
        expected_result = True
        assert Tests_exercise_1.exercise_1.number_is_prime(test_number) == expected_result

    def test_if_ten_is_prime_return_false(self):
        test_number = 10
        expected_result = False
        assert Tests_exercise_1.exercise_1.number_is_prime(test_number) == expected_result

    def test_if_thirteen_is_prime_return_true(self):
        test_number = 13
        expected_result = True
        assert Tests_exercise_1.exercise_1.number_is_prime(test_number) == expected_result
