# BST 의 특정 값 사이의 값들의 합
# DFS, 재귀
# 가지치기
# 참고


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            # not node
            if not node:
                return 0

            # node.val 이 low 보다 작을 경우 오른쪽만
            if node.val < low:
                return dfs(node.right)
            # node.val 이 high 보다 클 경우 왼쪽만
            if node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
