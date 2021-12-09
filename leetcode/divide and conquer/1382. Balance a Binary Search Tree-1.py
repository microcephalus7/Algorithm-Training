# BST 를 균형잡힌 (balanced) BST 로 바꾸기
# 재귀

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def balanceBST(self, root):

        # BST 를 정렬된 List 로 만들기
        # 참고 코드
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        nums = inorder(root)

        def constructBST(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])

            mid = len(nums) // 2

            new_node = TreeNode(nums[mid])

            new_node.left = constructBST(nums[:mid])
            new_node.right = constructBST(nums[mid+1:])

            return new_node

        return constructBST(nums)
