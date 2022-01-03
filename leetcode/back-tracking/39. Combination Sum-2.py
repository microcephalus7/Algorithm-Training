# 중복이 허용되는 조합의 합
# DFS, 백 트래킹
# 백트래킹 코드 참고

class Solution(object):
    def combinationSum(self, candidates, target):

        def dfs(nums, target, path):
            if target < 0:
                return
            if target == 0:
                ret.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], path+[nums[i]])

        ret = []
        dfs(candidates, target, [])
        return ret
