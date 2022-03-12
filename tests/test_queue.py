from code_challenges.stacks_and_queues.queue import Queue
import pytest

def test_enqueue():
    queue = Queue()
    queue.enqueue(5)
    expected = 5
    actual = queue.front.value
    assert expected == actual


def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = [1,2,3]
    actual = []
    actual.append(queue.front.value)
    actual.append(queue.front.next.value)
    actual.append(queue.front.next.next.value)
    assert expected == actual


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.dequeue()
    expected = 1
    assert actual == expected


def test_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = 1
    actual = queue.peek()
    assert expected == actual


def test_empty_queue_with_multiple_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    expected = None
    actual = queue.front
    assert expected == actual


def test_instantiate_empty_queue():
    queue = Queue()
    expected = None
    actual = queue.front
    assert expected == actual

def test_exception_raised_when_dequeue_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        queue.dequeue()

def test_exception_raised_when_peek_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        queue.peek()

