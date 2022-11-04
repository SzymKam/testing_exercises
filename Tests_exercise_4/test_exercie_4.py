from Tests_exercise_4.exercise_4 import Notebook
import pytest
# Dodanie, Remove, edit, clear_all, check_pos


class TestsNotebook:
    @pytest.fixture
    def setup_method(self, mocker):
        self.my_todos = []
        self.mocked_todo = mocker.patch("Tests_exercise_4.exercise_4.Notebook.todos", self.my_todos)
        # yield setup
        # self.my_todos.clear()

    def test_if_todo_len_is_right(self, setup_method):
        Notebook.add_todo("xyz")
        assert Notebook.todos == ["xyz"]

