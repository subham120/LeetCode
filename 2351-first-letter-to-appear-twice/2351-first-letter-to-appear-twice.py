class Solution:
    def repeatedCharacter(self, s: str) -> str:
        n = len(s)
        seen = ''
        for i in range(n):
            if s[i] in seen:
                return s[i]
            
            seen += s[i]