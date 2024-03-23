### Main Notes

[Unit 1](unit1_arrays.md) - Arrays

[Textbook (personal notes)](dsa_textbook_notes/README.md) - extra stuff.

-----

### Problems

 This page for now is problems that don't fit into units, but once we begin with picked problems,
 this will all move to "extra", and this section will 
be the master problem list, with short, one line comment, short, one line O(N).

Aim is to keep anything labeled "core" KISS, with only the problems and relevant DS/Alg to those problems listed,

**Two Sum**

- Use a [hash](../src/problems/two_sum.py) to store complements.

- O(N), O(N)

**Valid Parenthesis**

- [stack](../src/problems/valid_parenthesis.py)
- O(N), O(N)

**Merge Two Sorted Lists, Linked List**
- not sure how to put this in a sentence, but it's combining a ll, just do it.
- helpful to have a dummy node pointing at head
- O(N), O(1)

**Is Word Palindrome**
- `str.isalnum()` in python, `Character.isLetterOrDigit` in java
- can "cheat" with `return str == str[::-1]`, or `StringBuilder::reverse` in java
- O(N), O(1)

**Is Word Anagram Of Another Word**
- frequency counter with hash is O(N), O(1)
- sort both strings is O(NlogN), O(1)

**Invert Binary Tree?**
- need to review recursive and itera../src/dsa/sorting_algs/merge.pytive traversal


**Reverse Singly Linked List**

can be done [recursively](../src/dsa/structures/linked_lists.py#L30) for O(N), O(N):

- terminator is node or node.next null
- node.next.next = node; node.next = None

can be done iteratively for O(N), O(1):

**Add Two Integers, No +/-**
- `(a ^ b) + ((a & b) << 1)`
-   `xor`        `and`
- binary add - `and` gives the carry, `xor` gives the column digit
- O(N), O(1)

**Clinbing stairs (E)**
- it's just fibonacci (ONO1)

----

## search algorithms

moved to indiv. units

## sorting algorithms

moved to indiv. units.

## data structures

moved to indiv. units

## graph algs

probably not doing all these. At least will do Cycles, FCC (curacaos? think that's the drink), and review traversal

**cover?**

- Graph Traversal
- Finding Connected Components
- Dijkstra's
- Dijkstra's On Sparse Graphs
- Cycles
- Topological Sorting

## TODO

Now that this is going to be shared:

[ ] - Figure out Anki system (maybe just make cards at end of each "unit"?)

[ ] - Add problem text, links to code where helpful.

[X] - add in O(N) of everything

[X] - convert to a style that renders better (less bullet points) 

[X] - break this down into separate pages instead of one giant one
