class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        ans = []

        for i in range(len(arr) - 1):
            minDiff = min(minDiff, (arr[i + 1] - arr[i]))

        for i in range(len(arr) - 1):
            if minDiff == (arr[i + 1] - arr[i]):
                ans.append([arr[i], arr[i + 1]])

        return ans