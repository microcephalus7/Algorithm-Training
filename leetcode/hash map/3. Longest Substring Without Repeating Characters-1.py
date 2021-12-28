# 문자열에서 가장 긴 중복 없는 부분 문자열의 길이
# 슬라이딩 윈도우, 해시 테이블
# 보충 필요

class Solution:
    # abcabcaa
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length
