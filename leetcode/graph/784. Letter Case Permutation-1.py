# 대소문자 순열 (분화)
# 재귀 (DFS)
# is alpha

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def dfs(string: str, path: str):
            if not string:
                result.append(path)
                return

            char = string[0]
            splitted_string = string[1:]

            if string[0].isalpha():
                dfs(splitted_string, path + char.upper())
                dfs(splitted_string, path + char.lower())

            else:
                dfs(splitted_string, path + char)

        dfs(s, "")

        return result
