# Stacks and Queues
Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.

Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Stack
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.

Queue
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.


## API
Stack 

```push()```
- Arguments: value
- Adds a new node with that value to the top of the     stack with an O(1) Time performance.

```pop()```
- Arguments: none
- Returns: the value from node from the top of the stack
- Removes the node from the top of the stack. Should raise exception when called on empty stack

```peek()```
- Arguments: none
- Returns: Value of the node located at the top of the stack
- Should raise exception when called on empty stack
```is_empty()```
- Arguments: none
- Returns: Boolean indicating whether or not the stack is empty.

Queue

```enqueue()```
- Arguments: value
- Adds a new node with that value to the back of the queue with an O(1) Time performance.

```dequeue()```
- Arguments: none
- Returns: the value from node from the front of the queue
- Removes the node from the front of the queue should raise exception when called on empty queue

```peek()```
- Arguments: none
- Returns: Value of the node located at the front of the queue
- Should raise exception when called on empty stack 

```is_empty()```
- Arguments: none
- Returns: Boolean indicating whether or not the queue is empty