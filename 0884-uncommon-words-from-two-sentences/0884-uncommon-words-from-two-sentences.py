class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split() + s2.split()
        freq = Counter(words)
        return [word for word in words if freq[word] == 1]