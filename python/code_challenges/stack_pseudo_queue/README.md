# Challenge Summary
Create a new class called pseudo queue.
Do not use an existing Queue.
Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue


## Approach & Efficiency
My approach using 2 Stacks was to designate one stack as the "push stack" and the other as a "pop stack".


To handle enqueue operations I will simply add values to the "push stack"
The time complexity for this operation is O(1)

To handle dequeue operations I will handle three cases
- If pop stack is not empty, I will return the value on top of the pop stack
- If pop stack is empty, then I will transfer all values from push stack onto the pop stack then return the value on top of the pop stack
- If pop stack and push stack are both empty, then the PseudoQueue is empty and I will raise an exception
The time complexity for this operation is O(n) in the worst case with the possibility of it being O(1) in the best case


