class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] in 'aeiou':
                s = s[:-1]
                print('here')
            else:
                print('there')
                return s
        print('.')
        return ""