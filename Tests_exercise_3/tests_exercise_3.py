from Tests_exercise_3.exercise_3 import quick_sort
import pytest


class TestQuickSort:
    def test_quick_sort_empty_list(self):
        elements = []
        expected = []
        with pytest.raises(IndexError):
            assert quick_sort(arr=elements, end=len(elements)-1) == expected

    def test_quick_sort_list_of_equal_elements(self):
        elements = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = elements
        assert quick_sort(arr=elements, end=len(elements)-1) == expected

    def test_quick_sort_list_of_negative_and_positive_elements(self):
        elements = [10, -4, 3, 0, 1, -1, 8, -7]
        expected = [-7, -4, -1, 0, 1, 3, 8, 10]
        assert quick_sort(arr=elements, end=len(elements)-1) == expected

    def test_quick_sort_list_of_negative_elements(self):
        elements = [-1, -50, -1, -40, -3, -25, -5]
        expected = [-50, -40, -25, -5, -3, -1, -1]
        assert quick_sort(arr=elements, end=len(elements)-1) == expected

    def test_quick_sort_list_of_positive_elements(self):
        elements = [100, 99, 7, 54, 78, 5, 100, 1]
        expected = [1, 5, 7, 54, 78, 99, 100, 100]
        assert quick_sort(arr=elements, end=len(elements)-1) == expected
