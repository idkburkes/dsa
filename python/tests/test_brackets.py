import pytest
from code_challenges.stack_queue_brackets.brackets import validate_brackets


def test_one_bracket():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected

def test_three_brackets():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected

def test_extra_chars():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_nested_brackets():
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected

def test_nested_brackets_with_extra_chars():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

def test_no_closing_bracket():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected

def test_no_closing_bracket_and_no_opening_bracket():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected

def test_brackets_wrong_ordering():
    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected

def test_lone_opening_bracket():
    actual = validate_brackets("{")
    expected = False
    assert actual == expected

def test_lone_closing_bracket():
    actual = validate_brackets(")")
    expected = False
    assert actual == expected

def test_two_brackets_dont_match():
    actual = validate_brackets("[}")
    expected = False
    assert actual == expected