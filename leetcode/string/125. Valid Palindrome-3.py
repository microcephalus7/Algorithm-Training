# isalnum 이용

# 논리 순서
# 1. 반복문 돌며 isalnum
# 2. len 이용하여 처음, 끝에서부터 확인


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ""

        for char in s:
            if char.isalnum():
                filtered_string += char.lower()

        for index in range(len(filtered_string) // 2):

            if filtered_string[index] != filtered_string[len(filtered_string) - index - 1]:
                return False

        return True


solution = Solution()
solution.isPalindrome("A man, a plan, a canal: Panama")
