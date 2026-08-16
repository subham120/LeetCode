class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = Counter(s)
        counts = list(freq.values())
        counts.sort()
        d = len(freq) - k
        if d <= 0:
            return 0
        
        sum = 0
        for i in range(d):
            sum += counts[i]
            
        return sum