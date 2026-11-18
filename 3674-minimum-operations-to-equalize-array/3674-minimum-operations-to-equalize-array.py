class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = nums.count(nums[0])
        return 1 if freq < len(nums) else 0