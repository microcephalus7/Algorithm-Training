# 모든 부분 집합
# 백트래킹
# 최적화

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums: List, path: List):
            # path 에 넣을때 마다 삽입
            result.append(path)

            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]])

        dfs(arr, [])
        return result
