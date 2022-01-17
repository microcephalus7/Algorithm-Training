# 이진 트리의 최소 깊이

# BFS
# Queue
# 최적화
# 참고

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return depth
                else:
                    queue.append((node.left, depth + 1))
                    queue.append((node.right, depth + 1))
