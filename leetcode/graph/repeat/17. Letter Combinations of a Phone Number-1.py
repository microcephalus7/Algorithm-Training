# 전화번호 문자 조합한 순열
# DFS
# 참고

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def dfs(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for char in dict[digits[idx]]:

                dfs(idx + 1, path + char)

        dfs(0, "")

        return result
