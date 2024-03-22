class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """Review kadanes alg! I don't remember how this works"""
        max_array: int = nums[0]
        current_array: int = nums[0]

        for i in range(1, len(nums)):
            current_array = max(0, nums[i] + current_array)
            max_array = max(max_array, current_array)
        return max_array
