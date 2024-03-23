def maxSubArray(self, nums: list[int]) -> int:
    """
    Kadane's alg makes a lot more sense if you watch it work - there are good videos online.

    The idea is we have a running total that we just reset if it ever hits 0(A), but we keep storing the max we see (B)
    as we make the total. That means we're basically sliding a window up the left, and dumping everything to the left of
    it any time it goes negative.
    """
    max_seen: int = nums[0]
    running_total: int = nums[0]

    for i in range(1, len(nums)):
        running_total = max(0, nums[i] + running_total) # A
        max_seen = max(max_seen, running_total) # B
    return max_seen
