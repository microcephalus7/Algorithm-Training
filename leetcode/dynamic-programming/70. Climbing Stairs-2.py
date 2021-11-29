# 반복문

class Solution:

    def climbStairs(self, n: int) -> int:
        x, y = 1, 2

        for i in range(0, n - 1):
            x, y = y, x + y

        return x
