### Links

[textbook (personal notes)](dsa_textbook_notes/README.md)

[14 patterns to "ace interviews" link](https://leetcode.com/discuss/study-guide/4039411/14-Patterns-to-Ace-Any-Coding-Interview-Question)

-----
### Grind 75 week 1

**two sum**

- Use a [hash](../src/problems/two_sum.py) to store complements.

- O(N), O(N)

**valid parenthesis**

- [stack](../src/problems/valid_parenthesis.py)
- O(N), O(N)

**merge two sorted lists, linked list**
- not sure how to put this in a sentence, but it's combining a ll, just do it.
- helpful to have a dummy node pointing at head
- O(N), O(1)
    
**buy/sell stock**
- [sliding windowish](../src/problems/buy_sell_stock.py)
- left side moves by min (buy price), "right side" is just calculating the max profit
- O(N), O(1)

**is word palindrome**
- `str.isalnum()` in python, `Character.isLetterOrDigit` in java
- can "cheat" with `return str == str[::-1]`, or `StringBuilder::reverse` in java
- O(N), O(1)

**is word anagram of another word**
- frequency counter with hash is O(N), O(1)
- sort both strings is O(NlogN), O(1)

**Invert Binary Tree?**
- need to review recursive and iterative traversal

**binary search in sorted array**
- simple binary search, divide and conquer 
- sliding window left and right, calc mid each time, then turn left or right to mid +/- 1

##### Random problems worked

**reverse singly linked list**

can be done [recursively](../src/dsa/structures/linked_lists.py#L30) for O(N), O(N):

- terminator is node or node.next null
- node.next.next = node; node.next = None

can be done iteratively for O(N), O(1):

- TODO

**water in containers**
- sliding window. Increase the side that's lower.
- O(N), O(1)

**add two integers, no +/-**
- `(a ^ b) + ((a & b) << 1)`
-   `xor`        `and`
- binary add - `and` gives the carry, `xor` gives the column digit
- O(N), O(1)


**clinbing stairs (E)**
- it's just fibonacci (ONO1)

**contains duplicate**
- test length against a set creation, or just use a hash
- O(N), O(N)

**three sum?**

##### sorting algorithms

pick 2. For now it's merge and insertion. 

**insertion**
- O(N^2), O(1)
- this is the simple [swapper](../src/dsa/sorting_algs/insertion.py), left to right loop; swap i,j right to left until l[i]\>l[j]
- big numbers move left, swaps.
 
**merge O(NlogN), O(N)**
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
          left is mergeSort(first half of l1), right is mergeSort(second half of l2)
          return mergeTwoSortedLists(left, right)
    ```
                    
**bubble O(N^2), O(1)?**
- isn't this just a bad reverse insertion sort? 
 
**timsort (ONlogN), O(N)?**
- It's like a merge/insertion sort in one. Python uses it. Super fast for very specific cases (nearly sorted)
- something something cache coherence
  
**quicksort (ONlogN), O(logN)?**
- java uses a modified one of this (dual pivot?)
- pivots? 

----

### data structures

**ordered array**
- insertion/deletion is O(N) thanks to reshuffling
- search is O(log N) because [binary search](../src/textbook_work/Ch1_2_6_ordered_array.py#L22)

### graph algs

probably not doing all these. At least will do Cycles, FCC (curacaos? think that's the drink), and review traversal

**cover?**

- Graph Traversal
- Finding Connected Components
- Dijkstra's
- Dijkstra's On Sparse Graphs
- Cycles
- Topological Sorting

### TODO

Now that this is going to be shared:

[ ] - Figure out Anki system (maybe just make cards at end of each "unit"?)

[ ] - Add problem text, links to code where helpful.

[X] - add in O(N) of everything

[X] - convert to a style that renders better (less bullet points) 

[ ] - break this down into separate pages instead of one giant one
