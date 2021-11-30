# counter, max, min
# 최적화

class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            # counter 한 번만
            count = collections.Counter()
            for j in range(i, len(s)):
                count[s[j]] += 1
                values = count.values()
                result += max(values) - min(values)
        return result
