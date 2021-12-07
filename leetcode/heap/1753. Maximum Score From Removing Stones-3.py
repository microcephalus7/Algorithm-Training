# 파이썬 다운

class Solution:
    def maximumScore(self, a, b, c):
        s = sorted([a, b, c])

        if (s[0] + s[1]) <= s[2]:
            return int(s[0] + s[1])
        else:
            return int((a+b+c)/2)
