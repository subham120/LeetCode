class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 2:
            nums.sort()
            return nums[1]
        else:
            return -1