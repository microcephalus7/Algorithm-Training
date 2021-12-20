# 주어진 조건으로 문자열 삭제 반복 이 가능한 문자열 확인
# 브루트 포스

class Solution:
    def isValid(self, s: str) -> bool:
        t = ""

        while s != t:
            s, t = s.replace('abc', ''), s

        return s == ''
