# 문자열에서 모음만 뒤집기
# 투 포인터

class Solution:
    def reverseVowels(self, s):
        s = list(s)

        vows = set('aeiouAEIOU')

        left, right = 0, len(s) - 1

        while left < right:

            while left < right and s[left] not in vows:
                left += 1
            while left < right and s[right] not in vows:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        return ''.join(s)
