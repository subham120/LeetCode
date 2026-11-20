class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        ans = 0
        for l, r in pairwise(nums):
            if l == r:
                ans += 1
        
        return ans