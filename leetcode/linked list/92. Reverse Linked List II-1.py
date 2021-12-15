# 연결 리스트의 사이 값 뒤집기
# 반복

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        p = dummy = ListNode(0)
        dummy.next = head

        for _ in range(left - 1):
            p = p.next

        cur = p.next
        pre = None

        for _ in range(right - left + 1):
            cur.next, pre, cur = pre, cur, cur.next

        # 1 -> 2 <- 3 <- 4 5

        # cur = 5
        # pre = 4, 3, 2
        # 1, 2, 5
        p.next.next = cur
        # 1, 4, 3, 2
        # p.next = pre

        return dummy.next
