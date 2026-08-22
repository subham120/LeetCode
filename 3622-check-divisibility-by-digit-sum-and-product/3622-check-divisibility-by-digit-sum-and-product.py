class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        sum = 0
        mul = 1
        while n > 0:
            sum += n % 10
            mul *= n % 10
            n //= 10
        
        return num % (sum + mul) == 0