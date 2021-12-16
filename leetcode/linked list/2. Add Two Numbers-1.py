# 두 개의 역순 연결 리스트 더하기
# 전가산기
# 재귀
# 실패

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # l1 = [2, 4, 3]
    # l2 = [3, 4, 5]
    # l1 = [2, 3]
    # l2 = [4, 5 ,6 ,7]
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 and l2:
            share, rest = divmod(l1.val + l2.val, 10)
            node = ListNode(rest)

            node.next = self.addTwoNumbers(l1.next, l2.next)

            return node

        else:
            return l1 or l2
