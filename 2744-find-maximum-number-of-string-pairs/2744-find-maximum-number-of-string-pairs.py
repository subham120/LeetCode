class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[i][::-1] == words[j]:
                    count += 1
        
        return count