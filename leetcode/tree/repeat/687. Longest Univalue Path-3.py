# 가장 긴 같은 노드 길이
# DFS
# 재귀
# 변형

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, prev_val: int) -> int:
            if not node:
                return 0

            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)

            self.longest = max(self.longest, left + right)

            if node.val == prev_val:
                # 증가 코드
                # 참고
                return max(left, right) + 1
            else:
                return 0

        dfs(root, root.val)

        return self.longest
