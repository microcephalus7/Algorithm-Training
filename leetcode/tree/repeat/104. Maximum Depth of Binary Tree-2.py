# 이진 트리의 최고 깊이

# BFS,
# queue(deque)
# max

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_depth = 0
        queue = collections.deque([root])

        while queue:
            max_depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_depth
