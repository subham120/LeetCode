class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        mini = min(nums)
        res = []
        for num in range(mini, maxi):
            if num not in nums:
                res.append(num)
        
        return res