from functionality_code.operations import do_calculation
import pytest


# class TestWithoutMock:
#     """Do tests without using mock. Takes about 30s"""
#     def test_compute_for_positive_value(self):
#         expected = 105
#         actual = 5
#         assert do_calculation(actual) == expected
#
#     def test_compute_for_negative_value(self):
#         expected = 90
#         actual = -10
#         assert do_calculation(actual) == expected
#
#     def test_compute_for_zero_value(self):
#         expected = 100
#         actual = 0
#         assert do_calculation(actual) == expected


# class TestWithMock:
#     """Do tests with mock."""
#     def test_compute_for_positive_value(self, mocker):
#         expected = 105
#         actual = 5
#         mocker.patch('functionality_code.operations.call_api', return_value = 100)
#         assert do_calculation(actual) == expected
#
#     def test_compute_for_negative_value(self, mocker):
#         expected = 90
#         actual = -10
#         mocker.patch('functionality_code.operations.call_api', return_value=100)
#         assert do_calculation(actual) == expected
#
#     def test_compute_for_zero_value(self, mocker):
#         expected = 100
#         actual = 0
#         mocker.patch('functionality_code.operations.call_api', return_value=100)
#         assert do_calculation(actual) == expected


class TestWithMockAndFixture:
    """Do tests with mock and used fixture"""
    @pytest.fixture
    def set_call_api_mock(self, mocker):
        mocker.patch('functionality_code.operations.call_api', return_value=100)

    def test_compute_for_positive_value(self, set_call_api_mock):
        expected = 105
        actual = 5
        assert do_calculation(actual) == expected

    def test_compute_for_negative_value(self, set_call_api_mock):
        expected = 90
        actual = -10
        assert do_calculation(actual) == expected

    def test_compute_for_zero_value(self, set_call_api_mock):
        expected = 100
        actual = 0
        assert do_calculation(actual) == expected
