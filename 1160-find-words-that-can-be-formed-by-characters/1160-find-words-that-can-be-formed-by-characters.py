class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_freq = Counter(chars)
        res = 0
        for word in words:
            copy = chars_freq.copy()
            for char in word:
                if char in copy and copy[char] != 0:
                    copy[char] -= 1
                else:
                    res -= len(word)                    
                    break
            
            res += len(word)
        
        return res           