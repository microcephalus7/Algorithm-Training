# BST 를 GST 로 변환하기
# DFS,
# 중위 순위 탐색
# 참고

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            # 오른쪽
            root.right = self.bstToGst(root.right)
            # 중간
            self.val += root.val
            root.val = self.val
            # 왼쪽
            root.left = self.bstToGst(root.left)
        return root
