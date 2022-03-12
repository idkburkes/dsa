from code_challenges.stacks_and_queues.stack import Stack
import pytest

def test_push():
    stack = Stack()
    stack.push(5)
    actual = stack.top.value
    expected = 5
    assert actual == expected


def test_push_multiple():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    expected = [1,2,3]
    actual = []
    actual.append(stack.top.value)
    actual.append(stack.top.next.value)
    actual.append(stack.top.next.next.value)
    assert expected == actual


def test_pop():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    expected = 1
    actual = stack.pop()
    assert expected == actual


def test_empty_stack_with_multiple_pops():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.pop()
    stack.pop()
    stack.pop()
    expected = None
    actual = stack.top
    assert expected == actual


def test_peek():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    expected = 1
    actual = stack.peek()
    assert expected == actual


def test_instantiate_empty_stack():
    stack = Stack()
    expected = None
    actual = stack.top
    assert expected == actual


def test_exception_raised_when_pop_empty_stack():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()



def test_exception_raised_when_peek_empty_stack():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()
