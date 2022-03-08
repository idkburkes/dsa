
# Sorting Algorithms


## Insertion Sort



## Merge Sort




## Quicksort

Quicksort can be simplified into a few steps
- Determine a pivot value
- Partition the array based on the pivot (this is where most of the work is done)
- Divide and conquer
    - Apply quick sort on left half of the array
    - Apply quick sort on right half of the array

We'll use this array as an example

```[8,4,23,42,16,15]```

## Determine a pivot value

There are a few approaches to choosing a pivot value. One approach is to choose the median between the first number, the middle number, and the last number. A quick and easy solution is to use the last number in the array, this is what we'll do. 

Pivot = 15 (at index 5)

## Partition the array based on the pivot

"Partitioning" the array means moving the pivot value to its correct position in the array. In other words, this means to move the pivot value to a position where all of the numbers to the left of the pivot are less than or equal to the pivot, and all of the numbers to the right of the pivot are greater than the pivot.

We will accomplish this by iterating from the start of the array all the way to the pivot point. Keep track of a "wall" where all of the values to the left are less than the pivot. If a value is less than or equal to the pivot then swap it with whatever is currently after the "wall" and move the wall forward.

- [i] - current index
- [p] - pivot
- | - wall that represents the partition

Initial State 
|[i]------------------------[p]
```[8, 4, 23, 42, 16, 15]```
Wall starts at index -1, current index is 0, and we decided that the last number (15 at index 5) would be the pivot.

Iteration 1
In the first iteration we evaluate 8 to be less than 15. This means we'll swap the number at index i with the number directly after the wall at index 0 then increment the index of the wall. In this case the index i and the position of the wall are the same so there is no swap, but we still increment the index of the wall.
----|-[i]--------------------[p]
```[8, 4, 23, 42, 16, 15]```


Iteration 2
In the second iteration we evaluate 4 to be less than 15. At this point we swap the number at index i with the number directly afer the wall at index 1. In this case the index i and the position of the wall are the same so there is no swap. Since 4 is less than 15 we increment to position of the wall again.
---------|-[i]---------------[p]
```[8, 4, 23, 42, 16, 15]```


Iteration 3
In the third iteration we find that 23 is greather than 15 so there is no swap and no increment of the wall, we just move index i forward.
---------|-------[i]---------[p]
```[8, 4, 23, 42, 16, 15]```

Iteration 4
In the fourth iteration we find that 42 is greater than 15 so there is no swap and no increment of the wall, we just move index i forward.
---------|-------------[i]---[p]
```[8, 4, 23, 42, 16, 15]```

Iteration 5
In the fifth iteration we find that 16 is greater than 15 so there is no swap and no increment of the wall, we just move index i forward.
---------|------------------[ip]
```[8, 4, 23, 42, 16, 15]```

Iteration 6
In the sixth iteration index i is at the same location as the pivot. This is our signal to swap the pivot value with the number immediately after the partition wall. After this final swap we have moved 15 into its correct position within the array. 

```[8, 4, [15], 42, 16, 23]```

Divide and conquer

After 15 is moved to the correct position we can perform the same partitioning process on the left and right side of the arrays, essentially performing the inductive step on 2 subarrays.
[left]------[sorted]---------[right]
[8, 4] ------- [15] ------- [42, 16, 23]

After doing all these steps recursively the entire array will become sorted
