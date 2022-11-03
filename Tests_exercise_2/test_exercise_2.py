from Tests_exercise_2.exercise_2 import fizz_buzz


class TestFizzBuzz:
    def test_if_number_divisible_by_3_return_fizz(self):
        number = 9
        expected = 'fizz'
        assert fizz_buzz(number=number) == expected

    def test_if_number_divisible_by_5_return_buzz(self):
        number = 10
        expected = 'buzz'
        assert fizz_buzz(number=number) == expected

    def test_if_number_divisible_by_5_and_3_return_fizz_buzz(self):
        number = 15
        expected = 'fizzbuzz'
        assert fizz_buzz(number=number) == expected

    def test_if_number_0_return_nothing(self):
        number = 0
        expected = 0
        assert fizz_buzz(number=number) == expected

    def test_if_positive_number_return_nothing(self):
        number = 13
        expected = 0
        assert fizz_buzz(number=number) == expected

    def test_if_negative_return_nothing(self):
        number = -13
        expected = 0
        assert fizz_buzz(number=number) == expected
