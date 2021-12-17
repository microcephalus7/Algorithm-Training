# 페어 노드 스왑
# 노드 자체 스왑
# 재귀

# 참고

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1, 2, 3, 4


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next

            # 이전 노드에서 다음 노드를 묶음
            # 포인터 작업
            head.next = self.swapPairs(p.next)
            p.next = head
            return p

        return head
