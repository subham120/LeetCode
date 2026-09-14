class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        notPair = True
        for ch in s:
            if ch == '|' and notPair:
                notPair = False
            elif ch == '|':
                notPair = True
            if ch =='*' and notPair:
                ans += 1
            
        return ans