class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        ans = [item for pair in zip(pos, neg) for item in pair]
        return ans