class Solution:
    def minimumMoves(self, s: str) -> int:
        c=0
        i=0
        while i<len(s):
            if s[i]=="X":
                v=s[i:i+3]
                if "X" in v:
                    c+=1
                i+=3
            else:
                i+=1
        
        return c