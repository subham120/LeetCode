class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    ans.append(words[i])

        return list(set(ans))