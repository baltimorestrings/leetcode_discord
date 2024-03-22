# Todo now that we're sharing

[ ] - link to leetcode prob in vimwiki form, but..
[ ] - also just add in the problem text. Referential words don't scale past 20/30 cards
[ ] - add in O(N) of everything

# quicknotes

- water in containers (M)
    * sliding window. Increase the side that's lower.

- add two integers, no +/-
    * (a ^ b) + ((a & b) << 1)
    *   xor        and
    * binary add - `and` gives the carry, `xor` gives the column digit

- clinbing stairs (E)
    * it's just fibonacci

- buy/sell stock
    * sliding windowish
    * left side moves by min (buy price), "right side" is just calculating the max profit

- contains duplicate
    * test length against a set creation, or just use a hash

- two sum
    * hash

- three sum?

- merge two sorted lists, linked list
    * 


# sorting algs

- insertion - O(N^2)
  * this is the simple swapper, left to right loop; swap i,j right to left until l[i]\>l[j]
  * big numbers move left, swaps.
- 
- merge O(logN)
  * Recursion. Break loop in halves until recursed singles, assemble. Uses two functions:
  * mergeTwoSorgedLists(l1, l2) -> list 
  * mergeSort(l1): if l1.length is 1, return l1;
                 > otherwise: left is mergeSort(half of l1), right is mergeSort(... l2)
                 > return mergeTwoSortedLists(l1, l2)
- bubble O(N^2)?
  * isn't this just a bad reverse insertion sort? 
- 
- timsort?
  * It's like a merge/insertion sort in one. Python uses it.
  
- quicksort?

# graph algs

- curacao's alg? I think that's the drink. strongly connected components. 

- map color?

# algs algs?
