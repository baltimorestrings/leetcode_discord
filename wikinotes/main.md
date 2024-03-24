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

<details>
<summary>Problem</summary>

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
``` 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

</details>

<details>
<summary>Answer</summary>
```python3
def twoSum(nums: list[int], target: int) -> list[int]:
    """ for each num, we both check for (target - complement), then save its index """
    complements: dict[int, int] = {}
    for i in range(len(nums)):
        j = complements.get(nums[i])
        if j is not None:
            return (i, j)
        complements[target - nums[i]] = i
```

</details>

- Use a [hash](../src/problems/two_sum.py) to store complements.

- O(N), O(N) - the hash requires O(N) space for keys.

**Valid Parenthesis**

<details>
<summary>Problem</summary>
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

```
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

</details>


- use a [stack](../src/problems/valid_parenthesis.py)
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
