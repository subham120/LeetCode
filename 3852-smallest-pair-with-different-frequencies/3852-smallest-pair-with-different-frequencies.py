class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        small = min(nums)
        nums.sort()
        for num in nums:
            if num != small and freq[small] != freq[num]:
                return [small, num]

        return [-1, -1]