class Solution:
    def clearDigits(self, s: str) -> str:
        stack = ""
        for i in range(len(s)):
            if s[i].isalpha():
                stack += s[i]
            else:
                stack = stack[:-1]

        return stack