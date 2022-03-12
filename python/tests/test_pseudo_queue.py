import pytest
from code_challenges.stack_pseudo_queue.pseudo_queue import PseudoQueue


# Input - [10]->[15]->[20]
# Args - 5
# Output [5]->[10]->[15]->[20]	
def test_enqueue_multiple_values():
    pq = PseudoQueue()
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    pq.enqueue(5)
    actual = []
    for i in range(4):
        actual.append(pq.dequeue())
    expected = [20,15,10,5]
    assert actual == expected

# Input - 
# Args - 5
# Output - [5]
def test_enqueue_one_value():
    pq = PseudoQueue()
    pq.enqueue(5)
    actual = pq.dequeue()
    expected = 5
    assert actual == expected


# Input - [5]->[10]->[15]->[20]
# Output - 	20
# Internal State - [5]->[10]->[15]
def test_dequeue_one_value():
    pq = PseudoQueue()
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    pq.enqueue(5)
    actual = pq.dequeue()
    expected = 20
    assert actual == expected

# Input - [5]->[10]->[15]
# Output - 15
# Internal State - [5]->[10]
def test_dequeue_multiple_values():
    pq = PseudoQueue()
    pq.enqueue(15)
    pq.enqueue(10)
    pq.enqueue(5)
    actual = []
    for _ in range(3):
        actual.append(pq.dequeue())
    expected = [15,10,5]
    assert expected == actual


def test_dequeue_empty_raises_exception():
    with pytest.raises(Exception):
        pq = PseudoQueue()
        pq.dequeue()

def test_enqueue_multiple_then_queue_empty_raises_exception():
    with pytest.raises(Exception):
        pq = PseudoQueue()
        pq.enqueue(1)
        pq.enqueue(2)
        pq.enqueue(3)
        for _ in range(4):
            pq.dequeue()