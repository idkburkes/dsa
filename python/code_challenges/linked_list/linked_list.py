
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#Resubmit Code Challenge 5 - Linked List Implementation
class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def insert(self, value):
        node = Node(value, self.head)
        self.head = node

    def includes(self, target):
        cur = self.head
        while cur:
            if cur.val == target:
                return True
            cur = cur.next
        return False

    def __str__(self):
        res, cur = [], self.head
        while cur:
            res.append(f'{{{cur.val}}} -> ')
            cur = cur.next
        res.append('NULL') # last pointer in Linked-List is None
        return ''.join(res)

    def append(self, new_val):
        if self.head is None: #If linked-list is empty make this the head
            self.head = Node(new_val)
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = Node(new_val)

    #Resubmit Code Challenge 6
    def insert_before(self, target, new_val):
        if self.head and self.head.val == target: #inserting before first node
            new_node = Node(new_val, self.head)
            self.head = new_node
        elif self.head:
            current = self.head
            prev = Node(None, current)
            while(current and current.val != target): #traverse current and prev pointers
                current = current.next
                prev = prev.next
            if current and current.val == target: #target is found
                new_node = Node(new_val, current)
                prev.next = new_node
            else: #if this else block is reached we did not find target
                raise Exception('Target value not found in LinkedList')

    #Resubmit Code Challenge 6
    def insert_after(self, target, new_val):
        if self.head:
            current = self.head
            next_node = current.next
            while(current and current.next and current.val != target):
                current = current.next
                next_node = next_node.next
            if current and current.val == target:
                new_node = Node(new_val, next_node)
                current.next = new_node
            else: #if this else block is reached we did not find target
                raise Exception('Target value not found in LinkedList')

    # Resubmit Code Challenge 7
    def kth_from_end(self, k):
        if self.head is None:
            raise Exception('Linked List is empty')
        elif k < 0: 
            raise Exception('K is non positive integer')
        current, trail = self.head, self.head
        for _ in range(k):
            if current is None:
                raise Exception('No kth from the end exists in this Linked-List for k={k}')
            current = current.next
        while current.next:
            current = current.next
            trail = trail.next
        return trail.val

    @staticmethod
    def zip_lists(list1, list2):
        if list1.head is None and list2.head is None: return None
        elif list1.head is None: return list2
        elif list2.head is None: return list1
        head, ll1, ll2 = list1.head, list1.head, list2.head
        while ll1 and ll2:
            next = ll1.next
            ll1.next = ll2
            ll1 = next
            next = ll2.next
            if ll1:
                ll2.next = ll1
            ll2 = next
        return LinkedList(head)
        
        
        
        
        

