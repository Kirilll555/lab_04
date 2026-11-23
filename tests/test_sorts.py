from lab4.sorts import heap_sort, selection


def test_sort():
    arr = [5, 2, 8, 1, 9, -3, 0, 5]
    exp = [-3, 0, 1, 2, 5, 5, 8, 9]

    assert selection(arr) == exp
    assert heap_sort(arr) == exp
    assert arr == [5, 2, 8, 1, 9, -3, 0, 5]


def test_empty_and_one():
    assert selection([]) == []
    assert heap_sort([]) == []
    assert selection([1]) == [1]
    assert heap_sort([1]) == [1]


def test_sorted_and_reverse():
    assert selection([1, 2, 3]) == [1, 2, 3]
    assert heap_sort([1, 2, 3]) == [1, 2, 3]
    assert selection([3, 2, 1]) == [1, 2, 3]
    assert heap_sort([3, 2, 1]) == [1, 2, 3]


def test_dup():
    assert selection([2, 2, 1, 1, 2]) == [1, 1, 2, 2, 2]
    assert heap_sort([2, 2, 1, 1, 2]) == [1, 1, 2, 2, 2]