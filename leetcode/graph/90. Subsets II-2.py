# 중복 없는 부분집합
# 백트래킹

class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()

        def dfs(nums: List, path: List, count: int):
            if count == 0:
                result.append(path)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                dfs(nums[i + 1:], path + [nums[i]], count - 1)

        for i in range(len(arr) + 1):
            dfs(arr, [], i)

        return result
