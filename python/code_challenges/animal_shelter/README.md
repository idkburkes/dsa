# Challenge Summary
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.

Implement the following methods:
```python enqueue(animal)```
- Arguments: animal
    animal can be either a dog or a cat object.
```python dequeue(pref) ``` 
- Arguments: pref
    pref can be either "dog" or "cat"
- Return: either a dog or a cat, based on preference.
    If pref is not "dog" or "cat" then return null.


## Approach & Efficiency
I chose to use two separate collections for the cats and the dogs, for the dequeue method we'll check the preference
to decide which list we'll pop an element from. We'll pop an element from the front of the list with pop(0).
Enqueue and dequeue are both O(1) time operations
