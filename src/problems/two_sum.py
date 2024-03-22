class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """ O(N), O(N)
        hash (dict) takes up N space
        """
        complements: dict[int, int] = {}
        for i in range(len(nums)):
            j = complements.get(nums[i])
            if j is not None:
                return (i, j)
            complements[target - nums[i]] = i
