# isalnum 이용

# 논리 순서
# 1. 반복문 돌며 isalnum
# 2. 뒤집으며 비교

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ""

        for char in s:
            if char.isalnum():
                filtered_string += char.lower()

        return filtered_string == filtered_string[::-1]
