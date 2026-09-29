class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        for ch in set(word1 + word2):
            if abs(freq1[ch] - freq2[ch]) > 3:
                return False
            
        return True