# 띄엄띄엄 문자열 뒤집기
# 재귀
# 참고

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]

        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)
