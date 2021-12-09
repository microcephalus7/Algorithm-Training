# 피보나치
# 타뷸레이션
# 재귀

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n - 2)
