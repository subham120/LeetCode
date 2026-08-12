class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        idx = []
        for i in range(n):
            if s[i] == c:
                idx.append(i)
        
        res = [0] * n
        for i in range(n):
            if s[i] == c:
                res[i] = 0
            else:
                minIdx = float('inf')
                for j in idx:
                    minIdx = min(minIdx, abs(j - i))
                res[i] = minIdx
            
        return res