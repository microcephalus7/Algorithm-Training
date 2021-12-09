# 피보나치
# 타뷸레이션
# 재귀, 캐시

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]
