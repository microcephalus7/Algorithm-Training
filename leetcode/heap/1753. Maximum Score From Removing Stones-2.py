# 파이썬 다운

class Solution:
    def maximumScore(self, a, b, c):
        return min((a + b + c) / 2, a + b + c - max(a, b, c))
