class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            first = nums[i]
            second = nums[i + 1]
            if first + second in seen:
                return True
            seen.add(first + second)
        
        return False