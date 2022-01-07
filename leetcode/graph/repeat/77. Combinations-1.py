# n 개의 조합
# 백트래킹
# 참고

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(path: List, start: int, k: int):
            if k == 0:
                # 객체 복사
                result.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                dfs(path, i + 1, k - 1)
                # pop 으로 객체 복사 없이 사용
                # 참고
                path.pop()

        dfs([], 1, k)

        return result
