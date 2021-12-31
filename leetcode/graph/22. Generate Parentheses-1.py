# 괄호 생성하기
# DFS
# 실패
# 보충필요

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(path_len, path):
            if path_len == n:
                result.append(path)
                return
            mid = dfs()

        dfs(0, "")

        return result
