from Tests_exercise_4.exercise_4 import Notebook
import pytest


class TestsNotebook:
    @pytest.fixture
    def setup_method(self, mocker):
        self.my_todos = ['a', 'b', 'c', 'd']
        mocker.patch("Tests_exercise_4.exercise_4.Notebook.todos", self.my_todos)

    @pytest.mark.parametrize('element', ['abc', 'def', 'qrs', 'xyz'])
    def test_if_add_todo_is_right(self, setup_method, element):
        Notebook.add_todo(content=element)
        assert Notebook.todos == ['a', 'b', 'c', 'd', element]

    @pytest.mark.parametrize('position, result', [(0, ['b', 'c', 'd']), (1, ['a', 'c', 'd']),
                                                  (2, ['a', 'b', 'd']), (3, ['a', 'b', 'c'])])
    def test_if_remove_element_return_right_value(self, setup_method, position, result):
        Notebook.remove_todo(pos=position)
        assert Notebook.todos == result

    def test_if_remove_all_return_right_value(self, setup_method):
        Notebook.remove_all()
        assert Notebook.todos == []

    @pytest.mark.parametrize('position, content, expected', [(0, 'aaa', ['aaa', 'b', 'c', 'd']),
                                                             (1, 'bbb', ['a', 'bbb', 'c', 'd']),
                                                             (2, 'ccc', ['a', 'b', 'ccc', 'd']),
                                                             (3, 'ddd', ['a', 'b', 'c', 'ddd'])])
    def test_if_edit_todo_return_right_right_value(self, setup_method, position, content, expected):
        Notebook.edit_todo(pos=position, content=content)
        assert Notebook.todos == expected

    def test_if_check_position_return_right_value(self, setup_method):
        with pytest.raises(Exception):
            Notebook.check_pos(pos=10)

    def test_if_check_position_return_right_value_with_empty_todos(self, mocker):
        __my_todos = []
        __mocked_todo = mocker.patch("Tests_exercise_4.exercise_4.Notebook.todos", __my_todos)
        with pytest.raises(Exception):
            Notebook.check_pos(pos=0)
