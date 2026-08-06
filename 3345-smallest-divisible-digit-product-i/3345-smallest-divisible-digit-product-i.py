class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 11):
            num = i
            mul = 1
            while num > 0:
                mul *= num % 10
                num //= 10
            if mul % t == 0:
                return i