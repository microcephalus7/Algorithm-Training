# sort

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        values = []

        copy_head = head

        while copy_head:
            values.append(copy_head.val)
            copy_head = copy_head.next

        values.sort()

        copy_head = head

        for i in values:
            copy_head.val = i
            copy_head = copy_head.next

        return head
