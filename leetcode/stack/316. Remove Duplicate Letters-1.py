# 문자열에서 중복 문자 제거 후 사전식 순서로 나열
# 재귀
class Solution:
    def removeDuplicateLetters(self, s):

        # 집합으로 정렬
        for c in sorted(set(s)):
            suffix = s[s.index(c):]

            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))

        return ''
