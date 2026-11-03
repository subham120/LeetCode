class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        maxi = nums[0]
        for i in range(len(nums)):
            if nums[i] < maxi:
                count += (maxi - nums[i])
            elif nums[i] > maxi:
                count += i * (nums[i] - maxi)
                maxi = nums[i]

        return count