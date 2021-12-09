# 정규식 이용한 문자열 필터링

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
