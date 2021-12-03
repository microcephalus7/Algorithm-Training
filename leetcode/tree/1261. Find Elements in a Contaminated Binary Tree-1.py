# DFS, stack, in

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        stack = [[root, 0]]
        self.values = []

        while stack:
            node, value = stack.pop()
            node.val = value

            self.values.append(value)

            if node.left:
                stack.append([node.left, 2 * value + 1])
            if node.right:
                stack.append([node.right, 2 * value + 2])

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
