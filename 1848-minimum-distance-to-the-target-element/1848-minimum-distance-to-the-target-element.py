class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n//2+1):
            if nums[i] == target:
                ans = min(ans, abs(i - start))
            if nums[n - i - 1] == target:
                ans = min(ans, abs(n - i - 1 - start))
        
        return ans