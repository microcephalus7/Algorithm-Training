# 주어진 조건으로 문자열 삭제 반복 이 가능한 문자열 확인
# stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                else:
                    stack.pop()
                    stack.pop()
            else:
                stack.append(char)

        return not stack
