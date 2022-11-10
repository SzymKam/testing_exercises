from Tests_exercise_5.exercise_5 import calc_diff, datetime


class TestCalcDiffTest:
    def setup_method(self):
        self.case1 = {
            'start_time': '2021-11-03T09:22:28+00:00',  # result 0
            'end_time': '2021-11-03T09:22:28+00:00'
        }
        self.case2 = {
            'start_time': '2021-11-03T09:22:28+00:00',
            'end_time': '2021-11-04T09:22:28+00:00'
        }
        self.case3 = {
            'start_time': '2022-11-10 22:28+00:00',
            'end_time': None
        }

    def test_if_calc_diff_return_right_value_3(self, mocker):

        end_time = datetime.fromisoformat('2022-11-10 22:28+00:00')
        mock_datetime = mocker.patch("Tests_exercise_5.exercise_5.datetime")
        mocker.patch("Tests_exercise_5.exercise_5.datetime.now", return_value=end_time)
        mock_datetime.fromisoformat = datetime.fromisoformat

        assert calc_diff(case=self.case3) == 0

    def test_if_calc_diff_return_right_value_2(self):
        assert calc_diff(case=self.case2) == 86400

    def test_if_calc_diff_return_right_value_1(self):
        assert calc_diff(case=self.case1) == 0
