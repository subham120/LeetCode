class Solution:
    def arraySign(self, nums: list[int]) -> int:
        neg = 0
        for c in nums:
            if c == 0:
                return 0
            if c < 0:
                neg ^= 1
                
        return -1 if neg == 1 else 1