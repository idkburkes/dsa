import pytest
from code_challenges.hashtable.hashtable import HashTable
from code_challenges.linked_list.linked_list import Node, LinkedList


def test_hashtable_set():
    size = 1024
    prime = 3067
    hashtable = HashTable(size)
    key = 'Age'
    value = 25
    hashtable.set(key, value)

    # Manually hash the key
    sum = 0
    for i in range(3):
        char = key[i]
        sum += (ord(char) * (i+1))
    idx = (sum * prime) % size

    linkedlist = hashtable.buckets[idx]
    assert linkedlist is not None
    assert linkedlist.head.val == (key, value)

def test_hashtable_get(hashtable):
    expected = 25
    actual = hashtable.get('Age')
    assert expected == actual

def test_get_returns_null_for_key_not_present(hashtable):
    expected = None
    actual = hashtable.get('Key does not exist')
    return expected == actual

def test_get_unique_keys(hashtable):
    expected = {'Age', 'Name', 'Account Numbers'}
    actual = hashtable.keys()
    assert expected == actual

def test_handle_collision(hashtable_with_collision):  
    linkedlist = hashtable_with_collision.buckets[0]
    assert linkedlist.head.val == ('Test 2', 2)
    assert linkedlist.head.next.val == ('Test 1', 1)

def test_get_from_hashtable_with_collision(hashtable_with_collision):
    actual1 = hashtable_with_collision.get('Test 1')
    actual2 = hashtable_with_collision.get('Test 2')
    expected1 = 1
    expected2 = 2
    assert actual1 == expected1
    assert actual2 == expected2 

def test_hash_key_to_inrange_value():
    hashtable = HashTable()
    keys = [
        'Here', 'Are', 'Some', 'RANDOM', 'KEYS',
        'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
    ]
    for i in range(len(keys)):
        key = keys[i]
        idx = hashtable.hash(key)
        assert 0 <= idx < 1024

    
@pytest.fixture
def hashtable():
    hashtable = HashTable()
    hashtable.set('Age', 25)
    hashtable.set('Name', 'John Smith')
    hashtable.set('Account Numbers', [1,2,3,4,5])
    return hashtable

@pytest.fixture
def hashtable_with_collision():
    # Force a collision by setting size to 1
    hashtable = HashTable(1)
    hashtable.set('Test 1', 1)
    hashtable.set('Test 2', 2)
    return hashtable
