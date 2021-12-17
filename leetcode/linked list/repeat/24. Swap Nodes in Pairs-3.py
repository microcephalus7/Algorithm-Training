# 페어 노드 스왑
# 노드 자체 스왑
# 순회 전 노드가 가리키게 해야 함
# 반복

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:

            b = head.next
            head.next = b.next
            b.next = head

            # head 이전 노드가 b 가리켜야 함
            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next
