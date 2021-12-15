# 뒤에서 n번째 노드 삭제

# 런너
# n 만큼 빠른 slow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # head = [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]
    # n = 1, 4
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow = fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next

        return head
