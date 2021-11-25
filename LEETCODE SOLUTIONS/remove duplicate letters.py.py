remove duplicate letters.py

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {c : i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack: continue
            while stack and stack[-1] > c and lastIndex[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        return "".join(stack)