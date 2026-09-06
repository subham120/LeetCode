class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n1 = str(f"{num1:04d}")
        n2 = str(f"{num2:04d}")
        n3 = str(f"{num3:04d}")

        key = ""

        for i in range(4):
            key += min(n1[i], n2[i], n3[i])

        return int(key.lstrip('0')) if key.lstrip('0') else 0