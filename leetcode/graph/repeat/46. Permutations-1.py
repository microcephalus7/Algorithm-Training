# 순열
# 백트래킹

class Solution:
    def permute(self, nums):

        def dfs(arr, path):
            if not arr:
                result.append(path)

            for i in range(len(arr)):
                copy_arr = arr[:]

                del copy_arr[i]

                dfs(copy_arr, path+[arr[i]])

        result = []

        dfs(nums, [])

        return result
