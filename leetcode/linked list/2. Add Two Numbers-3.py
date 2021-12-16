# 두 개의 역순 연결 리스트 더하기
# 전가산기
# 반복
# 참고

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        share = 0

        # 셋 중 하나라도 있으면 순회하도록 함
        while l1 or l2 or share:
            sum = 0

            # l1이나 l2 있으면 next 로 넘어가게 함
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            share, rest = divmod(sum + share, 10)

            head.next = ListNode(rest)
            head = head.next

        return root.next
