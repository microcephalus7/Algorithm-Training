# DFS, max, recur

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, count: int):
            if node:
                self.max_depth = max(self.max_depth, count)
                if node.left:
                    dfs(node.left, count + 1)
                if node.right:
                    dfs(node.right, count + 1)

        dfs(root, 1)

        return self.max_depth
