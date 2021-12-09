# isalnum 을 이용한 알파벳/숫자 필터링

# isalnum, [::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ""

        for char in s:
            if char.isalnum():
                filtered_string += char.lower()

        return filtered_string == filtered_string[::-1]
