class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        setNums = set(nums)
        for i in range(1,102):
            if k * i not in setNums:
                return k * i