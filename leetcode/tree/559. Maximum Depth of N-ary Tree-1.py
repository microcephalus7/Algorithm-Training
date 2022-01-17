# 트리의 최고 깊이

# DFS
# 재귀

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    max_depth = 0

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        def dfs(node: Node, count: int):
            if node:
                self.max_depth = max(self.max_depth, count)

                if node.children:
                    for i in node.children:
                        dfs(i, count + 1)

        dfs(root, 1)

        return self.max_depth
