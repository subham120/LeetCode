class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if n * 9 < s:
            return -1

        ans = 0
        for i in range(n):
            x = min(s, 9)
            s -= x
            ans = ans * 10 + x

        return ans