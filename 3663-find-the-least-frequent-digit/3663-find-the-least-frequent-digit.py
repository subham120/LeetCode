class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        arr = [0] * 10
        while n > 0:
            digit = n % 10
            arr[digit] += 1
            n //= 10
        
        ans = 0
        minFreq = float('inf')

        for i in range(10):
            if arr[i] != 0 and arr[i] < minFreq:
                minFreq = arr[i]
                ans = i

        return ans