class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            
            if nums[i] == 0:
                if rightSum == leftSum:
                    count += 2
                elif abs(rightSum - leftSum) == 1:
                    count += 1
            
            leftSum += nums[i]

        return count