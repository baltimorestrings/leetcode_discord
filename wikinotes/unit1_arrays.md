# Unit 1 - Arrays

Back to [notes main](main.md)

---

Big O format note: O(N), O(N) is time and space complexity, in that order.

### Array Problems

**Two Sum**

- Use a [hash](../src/problems/two_sum.py) to store complements.

- O(N), O(N)

**Buy/Sell Stock**
- [sliding windowish](../src/problems/buy_sell_stock.py)
- left side moves by min (buy price), "right side" is just calculating the max profit
- O(N), O(1)
- *Extra*: There is an approach using Kadane's algorithm [here](../src/problems/buy_sell_stock.py#L15). 
  - the running total is of candles (stock changes), so the running total goes running + prices[i] - prices[i - 1]

**Contains Duplicate**
- test length against a set creation, or just use a hash
- O(N), O(N)

**Container Water**
- Sliding window ([full alg](../src/problems/water_containers.py))
- The "trick" is realizing that you just slide in either side, whichever
  is lower. The limiting factor is the lower one, so it's always good to do, 
- As you keep sliding the windows in towards each other, just keep tracking max encountered area.  
- O(N), O(1)

**Maximum Subarray**

- Kadane's Alg notes are below
- O(N), O(1)
- example [here](../src/problems/largest_subarray_add.py)

**Product of Array Except Self**

**Sort Colors**

The in place requirement means it isn't a sort.

need to do a sliding window swappy thing. Notes on it tomorrow and some practice.

**Binary Search in Sorted Array**

This one is simply know binary search. Will update this with a bit more example.

- simple binary search, divide and conquer
- know about using modulo to shift array:
  * a[-5 % len(a)], a[5 % len(a)] will shift a 5 to the left or right, wrapping as needed
- sliding window left and right, calc mid each time, then turn left or right to mid +/- 1

----

# Notes

----
### Data Structures

Not many for arrays.

**Sets/Maps/Dicts**

Hashes (dicts, sets) are O(N) space where N is keys. Access is effectively O(1) except in worst cases.

**Ordered Lists**

OrderedLists ([python](.../rc/textbook_work/Ch1_2_6_ordered_array.py)) are worth looking at solely because they
use binary search, mentioned in a few problems this unit. There are better ordered data structures that come later, so this isn't something to drill.

Since ordered lists use binary search, **search is O(log N)**, but note **insertion is O(N)** since an ordered list needs to be shuffled for adds/deletes.


### Search Algorithms

**Binary Search**

Classic sliding window, performed on sorted arrays

left = 0, right = n - 1, then throw away half at a time:
```
while (left <= right):
    mid = (left + right / 2)
    
    if target == array[mid]:
        return mid
    else:
        compare target with array[mid] 
        if it's less:
            make left = mid + 1
        if it's more:
            make right = mid - 1
```

- At the end, left is where you'd insert a new item if an ordered array.
- O(log N) O(1), because it just divides in 2 repeatedly and requires no space.
 
Examples here: [python](../src/textbook_work/Ch1_2_6_ordered_array.py#L22), [java](/../src/textbook_work/OrderedList.java#L54)

**Kadane's Algorithm**

This one is for the maximum subarray problem, however it can apply to the stock problem also.

Example and full explanation [here](../src/problems/largest_subarray_add.py)

```
running_total, max_seen = 0

for price in list_of_prices:
    add price to running_total
    if running_total is negative, reset it to 0
    if running_total is bigger than max_seen, set max_seen to it
    
```


---
### Sorting Algorithms

It is most likely fine if you learn one "good" sorting algorithm, but it's worth being able to 
at least mention the names of a few. 

Note that Quicksort is an "in place" sort, Merge is very much not since we break it down into a billion pieces.

**insertion**

- O(N^2), O(1)
- this is the simple [swapper](../src/dsa/sorting_algs/insertion.py), left to right loop; swap i,j right to left until l[i]\>l[j]
- big numbers move left, swaps.
 
**Merge Sort**

This one helps to inspect with breakpoints, or watch a video.

The first function is a simple zipper - it takes two sorted lists and assembles them with two pointers, zippering them up. No tricks there.

The second function will immediately recurse down, breaking everything up into lists of size 1, the idea
being that we have a function that assembles sorted lists, so we break it down into a bunch of size 1 lists, then assemble.

It has an nlogn time because it divides the list in half repeatedly, so you get that exponential
runaway, which makes sense, but note that since it's recursive, it will use up n stack frames, so you get that O(N) space.)

- O(n log n), O(N)
- [Recursion](../src/dsa/sorting_algs/merge.py).
- Break loop in halves until recursed singles, assemble. 
- Uses two functions:
 
    ```
    mergeTwoSorgedLists(l1, l2) -> list
        """ Expects l1 and l2 to be sorted lists, combines them into one list """
  
    mergeSort(l1):
      """ Recurses and breaks down an array into arrays of length 1, then assembles """
      if l1.length is 1:
          return l1
      otherwise:
          left is mergeSort(first half of l1)
          right is mergeSort(second half of l2)
          return mergeTwoSortedLists(left, right)
    ```
                    
**Bubble Sort**
- O(N^2), O(1)
- isn't this just a bad reverse insertion sort? 
 
**Timsort** 
- (ONlogN), O(N)?**
- It's like a merge/insertion sort in one. Python uses it. Super fast for very specific cases (nearly sorted)
- something something cache coherence
  
**Quicksort (ONlogN), O(logN)?**
- java uses a modified one of this (dual pivot something)
- pivots? 
