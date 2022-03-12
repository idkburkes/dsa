from code_challenges.stacks_and_queues.node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        if self.front:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.front = Node(value)
            self.rear = self.front


    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = temp.next
            temp.next = None # remove unnecessary reference
            return temp.value
        else:
            raise Exception('Cannot dequeue while queue is empty')



    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise Exception('Cannot peek while queue is empty')


    def is_empty(self):
        return self.front == None



    