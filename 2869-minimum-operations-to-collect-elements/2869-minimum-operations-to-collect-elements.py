class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        occurrence = []
        for i in range(n - 1, -1, -1):
            if nums[i] not in occurrence and nums[i] <= k:
                occurrence.append(nums[i])
            if len(occurrence) == k:
                return n - i