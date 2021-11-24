# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    check = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode):
            if not root:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.check = False

        dfs(root)

        return self.check
