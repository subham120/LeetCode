class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ""
        for ch in s:
            if len(stack) != 0:
                if ch == stack[-1]:
                    stack = stack[:-1]
                else:
                    stack += ch
            else:
                stack += ch

        return stack