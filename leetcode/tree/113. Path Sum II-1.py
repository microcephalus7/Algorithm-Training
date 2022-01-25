# root 노드 부터 leaf 노드의 값의 합이 타겟의 합 list
# DFS, 재귀

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        result = []

        def dfs(node, valSum, arr):
            if not node:
                return

            valSum += node.val

            arr = arr + [node.val]

            if not node.left and not node.right and valSum == targetSum:
                result.append(arr)
                return

            if node.left:
                dfs(node.left, valSum, arr)
            if node.right:
                dfs(node.right, valSum, arr)

        dfs(root, 0, [])

        return result
