# 반복문, for, DP

class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        third = None

        if n == 0:
            return first
        if n == 1:
            return second

        for i in range(n - 1):
            third = first + second
            first = second
            second = third

        return third
