from freezegun import freeze_time
from Tests_exercise_5.exercise_5 import calc_diff


class TestCalcDiff:
    @freeze_time('2022-11-04 22:28+00:00')
    def test_if_calc_diff_return_right_value(self):
        self.case = {
            'start_time': '2022-11-04 22:28+00:00',
            'end_time': None
        }
        assert calc_diff(self.case) == 0
