# isalnum, for


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
