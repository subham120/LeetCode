class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        char = set(s)
        for c in char:
            if s.rfind(c) - s.find(c) - 1 != distance[ord(c) - ord('a')]:
                return False
        
        return True