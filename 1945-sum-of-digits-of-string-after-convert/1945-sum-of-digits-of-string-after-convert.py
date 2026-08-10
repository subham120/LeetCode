class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = len(s)
        nums = ''
        for i in range(n):
            nums += str(ord(s[i]) - 96)
        
        num = int(nums)
        while k > 0:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            
            num = sum
            k -= 1

        return sum