class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = Counter(nums)
        for item, count in freq.items():
            if count == 1 and item % 2 == 0:
                return item
        
        return -1