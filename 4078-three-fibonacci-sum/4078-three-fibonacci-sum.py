class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n % 2 != 0:
            return False

        x = n // 2
        y = 5 * x * x + 4
        z = 5 * x * x - 4
        if int(y ** 0.5) ** 2 == y or int(z ** 0.5) ** 2 == z:
            return True
        
        return False