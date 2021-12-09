# 피보나치
# 타뷸레이션
# for

class Solution:

    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2

        for i in range(n - 1):
            first, second = second, first + second

        return first
