# 피보나치
# 타뷸레이션
# for

class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1

        for i in range(n):
            first, second = second, first + second

        return first
