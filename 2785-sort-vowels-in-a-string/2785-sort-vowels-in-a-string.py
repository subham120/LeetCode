class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = []
        for ch in s:
            if ch.lower() in 'aeiou':
                vowel.append(ch)
        
        vowel.sort()
        t = ''
        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                t += vowel.pop(0)
            else:
                t += s[i]

        return t