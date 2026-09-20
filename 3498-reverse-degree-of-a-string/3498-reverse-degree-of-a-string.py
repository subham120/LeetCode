class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        deg = 0
        for i in range(n):
            rev = 123 - ord(s[i])
            deg += rev * (i + 1)

        return deg