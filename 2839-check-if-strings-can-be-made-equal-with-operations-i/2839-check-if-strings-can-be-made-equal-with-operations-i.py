class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
            
        w1 = list(s1)
        w2 = list(s2)
        w3 = list(s1)

        w1[0], w1[2] = w1[2], w1[0]
        if w1 == w2:
            return True
        w1[1], w1[3] = w1[3], w1[1]
        if w1 == w2:
            return True
        w3[1], w3[3] = w3[3], w3[1]
        if w3 == w2:
            return True

        return False