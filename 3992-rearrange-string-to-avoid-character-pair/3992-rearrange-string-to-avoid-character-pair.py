class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if x < y:
            s = "".join(sorted(s, reverse=True))
        else:
            s = "".join(sorted(s))
        
        return s