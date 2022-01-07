# n 개의 조합
# 백트래킹

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(nums: List, path: List, count: int):
            if count == 0:
                result.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]], count - 1)

        dfs(range(1, n+1), [], k)

        return result
