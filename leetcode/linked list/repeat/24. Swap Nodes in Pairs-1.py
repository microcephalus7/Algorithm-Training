# 페어 노드 스왑
# 값만 스왑
# 반복

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        copy = head

        while copy and copy.next:
            copy.val, copy.next.val = copy.next.val, copy.val

            copy = copy.next.next

        return head
