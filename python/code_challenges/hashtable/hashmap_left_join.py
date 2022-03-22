from code_challenges.hashtable.hashtable import HashTable


def left_join(map1: HashTable, map2: HashTable, reverse_join=False):
    joined_map = HashTable()

    # Stretch goal to perform a right join
    if reverse_join:
        map1, map2 = map2, map1

    for key in map1.keys():
        pair = [map1.get(key)]
        if map2.contains(key):
            pair.append(map2.get(key))
        else:
            pair.append(None)
        
        joined_map.set(key, pair)
    
    return joined_map


