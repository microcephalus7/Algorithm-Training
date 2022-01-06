# 중복이 허용되는 조합의 합
# DFS, 백 트래킹
# 백트래킹 코드 참고
# 최적화

class Solution(object):
    def combinationSum(self, candidates, target):

        def dfs(nums, target, path):

            if target == 0:
                ret.append(path)
                return
            for i in range(len(nums)):

                # 점프 코드
                # 최적화
                if nums[i] > target:
                    break

                dfs(nums[i:], target-nums[i], path+[nums[i]])

        ret = []
        # 선 정렬
        dfs(sorted(candidates), target, [])
        return ret
