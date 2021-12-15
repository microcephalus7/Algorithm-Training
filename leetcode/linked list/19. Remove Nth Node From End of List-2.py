# 뒤에서 n번째 노드 삭제
# List 변환

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        del values[len(values)-n]

        dummy = p = ListNode(0)

        for i in values:
            p.next = ListNode(i)
            p = p.next

        return dummy.next
