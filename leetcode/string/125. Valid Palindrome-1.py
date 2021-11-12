# 정규식을 이용한 풀이

# 논리 순서
# 1. 선 변환 (전부 소문자)
# 2. 정규식으로 필터링
# 3. 뒤집은것과 같은지 확인

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
