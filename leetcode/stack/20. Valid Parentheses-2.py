# stack

# 비우기

# reverse

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in table:
                stack.append(table[char])
            else:
                if not stack or stack.pop() != char:
                    return False

        return len(stack) == 0
