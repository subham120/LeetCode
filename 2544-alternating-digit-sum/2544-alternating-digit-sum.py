class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        sign = 1
        for i in str(n):
            ans += sign * int(i)
            sign *= -1

        return ans