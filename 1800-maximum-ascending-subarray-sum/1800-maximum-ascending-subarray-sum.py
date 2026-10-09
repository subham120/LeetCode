class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        currSum = nums[0]
        res = currSum
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currSum += nums[i]
            else:
                currSum = nums[i]

            res = max(res, currSum)

        return res