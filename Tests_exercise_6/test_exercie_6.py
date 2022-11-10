import Tests_exercise_6.exercise_6
from Tests_exercise_6.exercise_6 import DbHandler, Config
import pytest


class TestDbHandler:
    @pytest.fixture
    def setup_elements(self, mocker):
        mocker.patch.object(Tests_exercise_6.exercise_6.Config, "DB_URL", "TEST_URL")
        mocker.patch.object(Tests_exercise_6.exercise_6.Config, "DB_USERNAME", "TEST_USERNAME")
        mocker.patch.object(Tests_exercise_6.exercise_6.Config, "DB_PASSWORD", "TEST_PASSWORD")
        mocker.patch.object(Tests_exercise_6.exercise_6.Config, "OK_MSG", "TEST_OK_MSG")
        mocker.patch.object(Tests_exercise_6.exercise_6.Config, "NOK_MSG", "TEST_NOK_MSG")

    def test_if_connect_to_database_return_right_value(self, setup_elements):
        assert DbHandler.connect_to_database() == f"I am connecting to TEST_URL as TEST_USERNAME " \
                                                  f"with pass: TEST_PASSWORD..."

    def test_if_show_msg_when_connected_return_right_value(self, setup_elements):
        test_db_handler = DbHandler()
        assert test_db_handler.show_msg_when_connected() == f"TEST_OK_MSG"

    def test_if_show_msg_when_interrupted_return_right_value(self, setup_elements):
        test_db_handler = DbHandler()
        assert test_db_handler.show_msg_when_interrupted() == f"TEST_NOK_MSG"

