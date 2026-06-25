class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ')': '(',
            '}': "{",
            ']': "["
        }

        for ch in s:
            if ch in parentheses:
                if not stack or stack.pop() != parentheses[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
        