# 이진 트리의 최소 깊이

# DFS
# 재귀

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_depth = sys.maxsize

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, count: int):

            if node:
                if not node.left and not node.right:
                    self.min_depth = min(self.min_depth, count)
                    return
                if node.left:
                    dfs(node.left, count + 1)
                if node.right:
                    dfs(node.right, count + 1)

        dfs(root, 1)

        return self.min_depth
