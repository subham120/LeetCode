class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)
        for i in range(len(num)):
            if int(num[i]) != freq[str(i)]:
                return False
        
        return True