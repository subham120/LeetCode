class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        setNum = set(nums)
        while True:
            if original in setNum:
                original *= 2
            else:
                break
        
        return original