# 최대값 index 이용한 이진 트리 만들기
# 재귀

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_num_index = nums.index(max(nums))

        new_node = TreeNode(nums[max_num_index])

        new_node.left = self.constructMaximumBinaryTree(nums[:max_num_index])
        new_node.right = self.constructMaximumBinaryTree(
            nums[max_num_index + 1:])

        return new_node
