class Solution:
    def maxDifference(self, s: str) -> int:
        ch=Counter(s)
        a=float('inf')
        b=0
        for x in ch.values():
            if x%2==0:
                a=min(a,x)
            else:
                b=max(b,x)
                
        return b-a