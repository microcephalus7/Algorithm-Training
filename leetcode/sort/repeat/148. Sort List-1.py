# sort
# 병합 정렬 연구 필요

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_copy = head

        values = []

        while head_copy:
            values.append(head_copy.val)
            head_copy = head_copy.next

        values.sort()

        head_copy = head

        for i in values:
            head_copy.val = i
            head_copy = head_copy.next

        return head
