
from code_challenges.stacks_and_queues.stack import Stack

class PseudoQueue():
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()
    
    def enqueue(self, value):
        self.pushStack.push(value)
    
    def dequeue(self):
        if not self.popStack.is_empty():
            return self.popStack.pop()
        elif not self.pushStack.is_empty():
            while not self.pushStack.is_empty():
                self.popStack.push(self.pushStack.pop())
            return self.popStack.pop()
        else:
            raise Exception('PseudoQueue is empty. Cannot dequeue value.')
            