from typing import Optional


def partition(array, i: int, j: int) -> int:
    """Define Pivot for Quick Sort method."""
    pivot_idx = (i + j) // 2
    pivot = array[pivot_idx]
    while i <= j:
        while pivot > array[i]:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return i


def quick_sort(arr, end: int, start: [int, Optional] = 0) -> None:
    """Sort list by the Quick Sort method."""
    edge = partition(array=arr, i=start, j=end)

    if start < edge - 1:
        quick_sort(arr, start=start, end=edge - 1)
    if end > edge:
        quick_sort(arr, start=edge, end=end)
    return arr
