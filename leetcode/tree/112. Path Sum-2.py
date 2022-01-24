# root 노드 부터 leaf 노드의 값의 합이 타겟의 합 있는지 판별
# DFS, 반복
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

        stack = [(root, root.val)]

        while stack:
            curr, val = stack.pop()

            if not curr.left and not curr.right and val == targetSum:
                return True

            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))

        return False
