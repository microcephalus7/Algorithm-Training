# 중복이 허용되지 않는 조합의 합
# DFS, 백 트래킹
# 백트래킹 코드 참고

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path):
            if target < 0:
                return

            if target == 0:
                ret.append(path)
                return

            for i in range(len(nums)):
                # 중복 점프 코드
                # 참조
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                # 점프 코드
                # 참조
                if nums[i] > target:
                    break

                dfs(nums[i + 1:], target-nums[i], path+[nums[i]])

        ret = []
        dfs(sorted(candidates), target, [])

        return ret
