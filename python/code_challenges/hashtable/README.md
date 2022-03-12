
# Hash Table Implementation


## Approach & Efficiency

My approach for the hash function was the sum the ascii values of characters, while also multplying each character by its index position in the key. This prevents us from having hash collisions for keys that aren't the same, but are permutations of the same characters. 

My approach for handling hash collisions was to implement a Linked-List data structure to store every key that has the same hash. This way if there is a collision, we can linearly traverse the linkedlist at the index of the hash that collided. This leaves us with a constant O(1) set operation and a O(c) get operation, where 'c' is the length of the linkedlist for all collisions at a particular index.


## Features

Implement a Hashtable Class with the following methods:

```set(key, value)```

- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.

```get(key)```

- Arguments: key
- Returns: Value associated with that key in the table

```contains(key)```

- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

```keys()```

- Returns: Collection of keys
hash
- Arguments: key
- Returns: Index in the collection for that key


## Testing

- Setting a key/value to your hashtable results in the value being in the data structure
- Retrieving based on a key returns the value stored
- Successfully returns null for a key that does not exist in the hashtable
- Successfully returns a list of all unique keys that exist in the hashtable
- Successfully handle a collision within the hashtable
- Successfully retrieve a value from a bucket within the hashtable that has a collision
- Successfully hash a key to an in-range value
