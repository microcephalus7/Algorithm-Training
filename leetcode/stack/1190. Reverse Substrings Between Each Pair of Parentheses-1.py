# 문자열에서 괄호 쳐저 있는 문자열 뒤집기
# stack

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for index, value in enumerate(s):
            if value == "(":
                stack.append("")

            elif value != ")":
                if stack:
                    stack[-1] = stack[-1] + value
                else:
                    stack.append(value)
            else:
                poped = stack.pop()[::-1]
                if stack:
                    stack[-1] = stack[-1] + poped
                else:
                    stack.append(poped)

        return stack[0]


solution = Solution()
print(solution.reverseParentheses("(abcd)"))
