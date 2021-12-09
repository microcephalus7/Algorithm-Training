# 문자열 2개로 가른 후 각자 다른 알파벳 몇개 있음?
# 메모이제이션
# counter

class Solution:
    def numSplits(self, s: str) -> int:
        left_count = collections.Counter()
        right_count = collections.Counter(s)

        result = 0

        for char in s:
            left_count[char] += 1
            right_count[char] -= 1

            if right_count[char] == 0:
                del right_count[char]

            if len(left_count) == len(right_count):
                result += 1

        return result
