# 균형잡힌 이진 트리 인지 확인
# DFS, 재귀
# 참고

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # -1 이 나올 시 되돌릴 수 없음
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        # return 값 확인
        return dfs(root) != -1
