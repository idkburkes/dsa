from readline import insert_text
from code_challenges.sorting_algos.insertion_sort import insertion_sort


def test_insertion_sort():
    actual =  [8, 4, 23, 42, 16, 15]
    insertion_sort(actual)
    expected = [4, 8, 15, 16, 23, 42] 
    assert actual == expected

def test_reverse_sorted():
    actual =  [20, 18, 12, 8, 5, -2]
    insertion_sort(actual)
    expected = [-2, 5, 8, 12, 18, 20] 
    assert actual == expected

def test_few_uniques():
    actual = [5, 12, 7, 5, 5, 7]
    insertion_sort(actual)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_nearly_sorted():
    actual = [2, 3, 5, 7, 13, 11]
    insertion_sort(actual)
    expected = [2,3,5,7,11,13]
    assert actual == expected