class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        return reduce(ior, nums)