# 모든 부분 집합
# 백트래킹

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums: List, path: List, count: int):
            if count == 0:
                result.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]], count - 1)

        for i in range(len(arr) + 1):
            dfs(arr, [], i)

        return result
