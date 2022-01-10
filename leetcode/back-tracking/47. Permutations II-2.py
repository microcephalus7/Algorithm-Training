# 순열 중 중복이 없는 결과값
# 백트래킹
# 최적화

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(arr, path):
            if not arr:
                result.append(path)
                return

            for i in range(len(arr)):
                # 점프 코드
                if i > 0 and arr[i] == arr[i - 1]:
                    continue

                dfs(arr[:i] + arr[i+1:], path + [arr[i]])

        # 정렬
        dfs(sorted(nums), [])

        return result
