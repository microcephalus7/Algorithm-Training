# 정렬된 연결 리스트 균형 이진트리로 변형
# DFS, 재귀
# 분할 정복

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        def dfs(arr):
            if not arr:
                return None

            mid = len(arr) // 2

            node = TreeNode(arr[mid])
            node.left = dfs(arr[:mid])
            node.right = dfs(arr[mid + 1:])

            return node

        return dfs(nums)
