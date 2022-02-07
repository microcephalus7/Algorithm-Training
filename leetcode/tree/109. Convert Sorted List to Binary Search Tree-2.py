# 정렬된 연결 리스트 균형 이진트리로 변형
# DFS, 재귀
# 런너, 분할 정복
# 참고

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
            return
        if not head.next:
            return TreeNode(head.val)

        # 런너
        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 뒷쪽
        tmp = slow.next

        # 커팅
        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root
