# 유효한 괄호
# stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in dict:
                stack.append(dict[char])
            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
