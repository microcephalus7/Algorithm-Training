# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val_sum: int = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return

        def dfs(node):
            if low <= node.val <= high:
                self.val_sum += node.val

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)

        return self.val_sum
