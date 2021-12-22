# 문자열에서 괄호 쳐저 있는 문자열 뒤집기
# stack
# 리팩토링
# 참고

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for index, value in enumerate(s):
            if value == "(":
                stack.append("")

            elif value != ")":
                stack[-1] += value

            else:
                poped = stack.pop()[::-1]
                stack[-1] += poped

        return "".join(stack)


solution = Solution()
print(solution.reverseParentheses("(abcd)"))
