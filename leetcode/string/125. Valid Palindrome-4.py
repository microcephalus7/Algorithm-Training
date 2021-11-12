# deque 이용

# 논리 순서
# 1. 반복문 돌며 isalnum
# 2. pop, popleft 으로 비교


from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                filtered_chars.append(char.lower())

        while len(filtered_chars) > 1:
            if filtered_chars.pop() != filtered_chars.popleft():
                return False

        return True


solution = Solution()
solution.isPalindrome("A man, a plan, a canal: Panama")
