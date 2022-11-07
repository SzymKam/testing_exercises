import pytest

from Tests_exercise_5 import exercise_5
from Tests_exercise_5.exercise_5 import calc_diff


class TestCalcDiff:
    @pytest.fixture
    def setup_test(self, mocker):
        self.actual_timedate = '2022-11-04T09:22:28+00:00'
        mocker.patch.object(exercise_5.calc_diff, 'datetime.now()', self.actual_timedate)

        self.case1 = {
            'start_time': '2021-11-03T09:22:28+00:00',   # result 0
            'end_time': '2021-11-03T09:22:28+00:00'
                }
        self.case2 = {
            'start_time': '2021-11-03T09:22:28+00:00',  # result 86400
            'end_time': '2021-11-04T09:22:28+00:00'
        }
        self.case3 = {
            'start_time': '2022-11-04T09:22:28+00:00',  # result 86400
            'end_time': None
        }

    def test_if_calc_diff_return_right_value(self, setup_test):
        assert calc_diff(case=self.case3) == 0
