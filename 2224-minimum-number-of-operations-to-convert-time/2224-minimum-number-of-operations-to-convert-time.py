class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        t1 = int(current[:2]) * 60 + int(current[3:])
        t2 = int(correct[:2]) * 60 + int(correct[3:])

        diff = t2 - t1
        count = 0

        for i in [60, 15, 5, 1]:
            count += diff // i
            diff %= i

        return count