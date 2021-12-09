# 피보나치
# 타뷸레이션
# 재귀
# time out

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n - 2)
