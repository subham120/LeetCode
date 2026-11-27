class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        c = Counter(nums)
        ans = -1
        maxi = 0

        for k, v in c.items():
            if k % 2 == 0:
                if v > maxi or (v == maxi and k < ans):
                    maxi = v
                    ans = k

        return ans