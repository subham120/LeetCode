class Solution:
    def splitNum(self, num: int) -> int:

        sortNum = sorted(list(map(int, str(num))))
        n = len(sortNum)

        num1 = []
        num2 = []

        for i in range(n):
            if i % 2 == 0:
                num2.append(sortNum[i])
            else:
                num1.append(sortNum[i])


        return int("".join(map(str, num1))) + int("".join(map(str, num2)))