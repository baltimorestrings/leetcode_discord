# Unit 1 - Arrays

Back to [notes main](main.md)

---

Big O format note: O(N), O(N) is time and space complexity, in that order.

### Array Problems

**1929. Concatenate Two Arrays**

Don't really know what to write here. Join the arrays!

<details><summary>Problem</summary>

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 
```
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
```

</details>

<details><summary>Answer</summary>

```python3
def getConcat(nums: list[int]) -> list[int]:
    return nums * 2  # in a real interview, I suggest manually making the new array
```

</details>

**27. Remove Element**

<details><summary>Problem</summary>
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 
```
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
````

</details>

<details><summary>Answer</summary>

```python3
def removeElement(nums: list[int], val: int) -> int:
  """ we're just going to scan for non-val numbers, print them at cursor as needed.
    cursor = scanner = 0
    while scanner < len(nums):
        if nums[scanner] != val:
            if scanner != cursor:
                nums[cursor] = nums[scanner]
            scanner += 1
            cursor += 1
        else:
            scanner += 1
    return cursor
```

</details>

- note that it wants the array modified in place, so this has to be two pointers.
- just have one pointer as "print cursor" and one pointer as "scanner", swap as needed.

**26. Remove Duplicates from Sorted array**

<details><summary>Problem</summary>

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 
```
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
```
</details>

<details><summary>Answer</summary>

```python3
def removeDuplicates(nums: List[int]) -> int:
   cursor = scanner = 1
   while scanner < len(nums):
       if nums[scanner] == nums[cursor - 1]:
           scanner += 1
       else:
           if cursor != scanner:
               nums[cursor] = nums[scanner]
           scanner += 1
           cursor += 1
   return cursor

```
</details>

- two pointers, scanner, cursor
- print at cursor as scanner sees values that aren't cursor - 1
 
**1. Two Sum**


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

- O(N), O(N)

**121. Buy/Sell Stock**

<details>
<summary>Problem</summary>

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

```
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

```
</details>
<details>
<summary>Answer</summary>

##### sliding window

```python3
def maxProfit(prices: list[int]) -> int:
    """
    We will track two things, lowest price seen (A), and max profit (B) we can make on the current one.

    We just keep retesting B on each one, and grabbing each new lowest stock point, and we're guaranteed to capture
    the longest line.
    """
    max_profit = 0
    buy_price = float('inf')
    for i in range(0, len(prices)):
        buy_price = min(buy_price, prices[i]) # A
        max_profit = max(max_profit, prices[i] - buy_price) # B
    return max_profit
```

##### kadanes (see max subarray)
```python3
def maxProfit2(prices: list[int]) -> int:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4868897/most-optimized-kadane-s-algorithm-java-c-python-rust-javascript/

    This is also O(N), O(1). Included it for completionism, but the first way is fine. Kadane's will come up in the
    largest subarray problem, so I figured might want it later.
    """
    n = len(prices)
    maxProfit = 0
    currMax_Profit = 0

    for i in range(1, n):
        currMax_Profit += prices[i] - prices[i - 1]

        if currMax_Profit > 0:
            pass

        else:
            currMax_Profit = 0

        maxProfit = max(maxProfit, currMax_Profit)

    return maxProfit
```
</details>


- [sliding windowish](../src/problems/buy_sell_stock.py)
- left side moves by min (buy price), "right side" is just calculating the max profit
- O(N), O(1)
- *Extra*: There is an approach using Kadane's algorithm [here](../src/problems/buy_sell_stock.py#L15). 
  - the running total is of candles (stock changes), so the running total goes running + prices[i] - prices[i - 1]

**217. Contains Duplicate**
- test length against a set creation, or just use a hash
- O(N), O(N)

**Container Water**

<details>
<summary>Problem</summary>
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


```
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
```
</details>

<details>
<summary>Answer</summary>

```python3
def maxArea(heights: list[int]) -> int:
    """
    A is the vertical side of the water, B is the width.

    Algorithm is to simply sliding window, track the max, and just keep moving in the shorter side (C)
    """
    left: int = 0
    right: int = len(heights) - 1

    max_area = min(heights[left], heights[right]) * (right - left)
    """         A                                   B              """

    while left < right:
        max_area = max(
            min(heights[left], heights[right]) * (right - left),  # A
            max_area  # B
        )
        if heights[left] < heights[right]:  # C
            left += 1
        else:
            right -= 1
    return max_area
```
</details>


- Sliding window ([full alg](../src/problems/water_containers.py))
- The "trick" is realizing that you just slide in either side, whichever
  is lower. The limiting factor is the lower one, so it's always good to do, 
- As you keep sliding the windows in towards each other, just keep tracking max encountered area.  
- O(N), O(1)

**53. Maximum Subarray**

<details>
<summary>Problem</summary>
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

```
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
```
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

</details>

<details>
<summary>Answer</summary>

        
```python3
def maxSubArray(nums: list[int]) -> int:
    """
    Kadane's alg makes a lot more sense if you watch it work - there are good videos online.

    The idea is we have a running total that we just reset if it ever hits 0(A), but we keep storing the max we see (B)
    as we make the total. That means we're basically sliding a window up the left, and dumping everything to the left of
    it any time it goes negative.
    """
    max_seen: int = float('-inf')
    running_total: int = 0

    for i in range(0, len(nums)):
        running_total += nums[i]
        max_seen = max(max_seen, running_total)
        running_total = max(0, running_total)
    
    return max_seen
```

</details>


- Kadane's Alg notes are below
- O(N), O(1)
- example [here](../src/problems/largest_subarray_add.py)

**238. Product of Array Except Self**


**75.Sort Colors**

The in place requirement means it isn't a sort.

need to do a sliding window swappy thing. Notes on it tomorrow and some practice.

**704. Binary Search in Sorted Array**

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

**Ordered lists**

Orderedlists ([python](.../rc/textbook_work/Ch1_2_6_ordered_array.py)) are worth looking at solely because they
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
 
Examples here: [python](../src/textbook_work/Ch1_2_6_ordered_array.py#L22), [java](/../src/textbook_work/Orderedlist.java#L54)

**Kadane's Algorithm**

This one is for the maximum subarray problem, however it can apply to the stock problem also.

Example and full explanation [here](../src/problems/largest_subarray_add.py)

```
max_so_far = -infinite
running_total = 0

for price in list_of_prices:
    add price to running_total
    if running_total is bigger than max_so_far, update max_so_far to it
    if running_total is negative, reset it to 0
    
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
    mergeTwoSorgedlists(l1, l2) -> list
        """ Expects l1 and l2 to be sorted lists, combines them into one list """
  
    mergeSort(l1):
      """ Recurses and breaks down an array into arrays of length 1, then assembles """
      if l1.length is 1:
          return l1
      otherwise:
          left is mergeSort(first half of l1)
          right is mergeSort(second half of l2)
          return mergeTwoSortedlists(left, right)
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
