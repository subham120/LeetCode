class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word: str) -> int:
            num_str = ""
            for char in word:
                num_str += str(ord(char) - ord('a'))
            return int(num_str)
        
        return (convert(firstWord) + convert(secondWord)) == convert(targetWord)