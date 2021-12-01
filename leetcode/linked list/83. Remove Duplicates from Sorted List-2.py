# while, 최적화

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node is not None and node.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
