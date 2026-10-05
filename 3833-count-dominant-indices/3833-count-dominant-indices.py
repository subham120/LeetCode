class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 1):
            if nums[i] > sum(nums[i+1:n])/(n-i-1):
                count += 1
        
        return count