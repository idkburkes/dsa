from code_challenges.stacks_and_queues.node import Node


class Stack:

    def __init__(self):
        self.top = None


    def push(self, value):
        if self.top:
            node = Node(value, self.top)
            self.top = node
        else:
            self.top = Node(value)


    def pop(self):
        if self.top:
            temp = self.top
            self.top = temp.next
            temp.next = None # remove unnecessary reference
            return temp.value
        else:
            raise Exception('Cannot pop while stack is empty')


    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise Exception('Cannot peek while stack is empty')


    def is_empty(self):
        return self.top == None
