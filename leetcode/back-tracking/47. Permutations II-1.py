# 순열 중 중복이 없는 결과값
# 백트래킹

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(arr, path):
            if not arr:
                if path not in result:
                    result.append(path)
                return

            for i in range(len(arr)):

                dfs(arr[:i] + arr[i+1:], path + [arr[i]])

        dfs(nums, [])

        return result
