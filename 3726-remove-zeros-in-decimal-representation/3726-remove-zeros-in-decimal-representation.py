class Solution:
    def removeZeros(self, n: int) -> int:
        num = str(n)
        ans = ''
        for i in num:
            if i != '0':
                ans += i
        
        return int(ans)