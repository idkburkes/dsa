from code_challenges.sorting_algos.quicksort import quicksort


def test_quicksort():
    actual = [8,4,23,42,16,15]
    quicksort(actual, 0, 5)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_reverse_sorted():
    actual = [20,18,12,8,5,-2]
    quicksort(actual, 0, 5)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_few_uniques():
    actual = [5,12,7,5,5,7]
    quicksort(actual, 0, 5)
    expected = [5,5,5,7,7,12]
    assert actual == expected 

def test_nearly_sorted():
    actual = [2,3,5,7,13,11]
    quicksort(actual, 0, 5)
    expected = [2,3,5,7,11,13]
    assert actual == expected