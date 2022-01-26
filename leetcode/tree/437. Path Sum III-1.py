# 노드들의 값의 합이 타겟의 합 count
# DFS, 재귀
# 보충 필요

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, targetSum, [targetSum])

    def dfs(self, node, origin, targets):
        if not node:
            return 0

        hit = 0

        for target in targets:
            if not target - node.val:
                hit += 1

        targets = [target - node.val for target in targets] + [origin]

        return hit + self.dfs(node.left, origin, targets) + self.dfs(node.right, origin, targets)
