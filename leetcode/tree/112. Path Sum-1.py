# root 노드 부터 leaf 노드의 값의 합이 타겟의 합 있는지 판별
# DFS, 재귀
# 참고

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # leaf 노드 판별
        # 참고
        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        # True or False return
        # 참고
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
