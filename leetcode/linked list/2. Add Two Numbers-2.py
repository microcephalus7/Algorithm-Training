# 두 개의 역순 연결 리스트 더하기
# 전가산기
# 재귀
# 참고

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        share, rest = divmod(l1.val + l2.val, 10)

        node = ListNode(rest)

        # any 로 셋 중 하나라도 있으면 재귀
        if any((l1.next, l2.next, share)):
            # 없으면 만들었음
            # next 를 함수 호출 때가 아니라 미리 함
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)

            l1.val += share

            node.next = self.addTwoNumbers(l1, l2)

        return node
