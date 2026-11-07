class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        smallest = float('inf')
        for i in range(0, len(nums), 2):
            smallest = min(smallest, nums[i] * 10 ** len(str(nums[i + 1])) + nums[i + 1])
        
        return smallest