class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        largest = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = largest
            if curr > largest:
                largest = curr

        return arr