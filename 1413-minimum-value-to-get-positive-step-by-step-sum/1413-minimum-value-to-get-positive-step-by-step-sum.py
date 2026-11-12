class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        total = 0
        lowest = 0
        for x in nums:
            total += x
            lowest = min(lowest, total)
            
        return 1 - lowest