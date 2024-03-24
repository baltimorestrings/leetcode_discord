def maxSubArray(nums: list[int]) -> int:
    """
    Kadane's alg makes a lot more sense if you watch it work - there are good videos online.

    The idea is we have a running total that we just reset if it ever hits 0(A), but we keep storing the max we see (B)
    as we make the total. That means we're basically sliding a window up the left, and dumping everything to the left of
    it any time it goes negative.
    """
    max_seen = float('-inf')
    max_ending_here = float('-inf')

    for num in nums:
        max_ending_here += num
        max_seen = max(max_seen, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_seen
