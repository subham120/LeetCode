class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(1, n + 1, 2):
            for j in range(n - i + 1):
                ans += sum(arr[j:j + i])

        return ans