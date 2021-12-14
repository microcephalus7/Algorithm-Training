# 연결 리스트의 사이 값 뒤집기

# 반복문

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1 2 3 4 5
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node

        #
        for i in range(left - 1):
            pre = pre.next

        reverse = None

        cur = pre.next

        for i in range(right - left + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummy_node.next
