from code_challenges.hashtable.hashtable import HashTable
from code_challenges.hashtable.hashmap_left_join import left_join
import pytest


def test_left_join(test_map1, test_map2):
    
    left_joined_map = left_join(test_map1, test_map2)

    assert left_joined_map.get('fond') == ['enamored', 'averse']
    assert left_joined_map.get('wrath') == ['anger', 'delight']
    assert left_joined_map.get('diligent') == ['employed', 'idle']
    assert left_joined_map.get('outfit') == ['garb', None]
    assert left_joined_map.get('guide') == ['usher', 'follow']
    

@pytest.fixture
def test_map1():
    map = HashTable()
    map.set('diligent', 'employed')
    map.set('fond', 'enamored')
    map.set('guide', 'usher')
    map.set('outfit', 'garb')
    map.set('wrath', 'anger')
    return map

@pytest.fixture
def test_map2():
    map = HashTable()
    map.set('diligent', 'idle')
    map.set('fond', 'averse')
    map.set('guide', 'follow')
    map.set('flow', 'jam')
    map.set('wrath', 'delight')
    return map

