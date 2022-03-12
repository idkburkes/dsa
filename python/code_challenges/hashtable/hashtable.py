from code_challenges.linked_list.linked_list import LinkedList, Node


class HashTable():

    def __init__(self, size=1024):
        self.buckets = [None] * size
        self.curkeys = set()
        self.size = size

        # Random prime number to use for hash function
        self.prime = 3067

    def set(self, key, value):
        idx = self.hash(key)

        # Init linked-list if index has no keys yet
        if self.buckets[idx] is None:
            self.buckets[idx] = LinkedList()
        
        linkedlist = self.buckets[idx]

        if key in self.curkeys:
            # Remove previous key-value pair
            node = linkedlist.head
            prev = Node(None, node)

            # Find key-value pair
            while node and node.val != value:
                node = node.next
                prev = prev.next

            if prev is None:
                # Remove First Node
                linkedlist.head = node.next
            elif node.next is None:
                 # Remove Last Node
                 prev.next = None
            else:
                # Remove Middle Node
                prev.next = node.next
        else:
            self.curkeys.add(key)

        # Insert new key-value pair
        linkedlist.insert((key, value))

        

    def get(self, key):
        idx = self.hash(key)

        # Key does not exist
        if self.buckets[idx] is None:
            return None

        linkedlist = self.buckets[idx]

        # Linear traverse bucket to find key-value pair
        node = linkedlist.head
        while node:
            pair = node.val
            if pair[0] == key:
                return pair[1]
            node = node.next
        
        # Key was not found
        return None


    def contains(self, key):
        value = self.get(key)
        return value != None

    def keys(self):
        return self.curkeys

    # Calculate hashes and indices by summing the ascii values of each character
    # Also multiply each ascii value by current index of key to avoid collisions
    # for permutations of the same characters
    def hash(self, key):
        sum = 0
        n = len(key)

        for i in range(n):
            char = key[i]
            sum += (ord(char) * (i+1))

        idx = (sum * self.prime) % self.size
        return idx

    
