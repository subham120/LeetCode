class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = inf
        for i in range(n):
            for j in range(n):
                if nums[i] == 1 and nums[j] == 2:
                    ans = min(ans, abs(i - j))
                if nums[i] == 2 and nums[j] == 1:
                    ans = min(ans, abs(i - j))
        
        return ans if ans != inf else -1