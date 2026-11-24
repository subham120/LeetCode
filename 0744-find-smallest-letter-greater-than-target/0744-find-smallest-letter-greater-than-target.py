class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        l = 0
        r = n - 1
        ans = n
        while l <= r:
            mid = l + (r - l) // 2
            if target < letters[mid]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return letters[ans % n]