# k 번째 노드, Len - k 번쨰 노드 스왑
# 값만 바꾸기
# 반복
# 참고

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head

        for i in range(k - 1):
            first = first.next

        null_checker = first

        while null_checker.next:
            last = last.next
            null_checker = null_checker.next

        first.val, last.val = last.val, first.val

        return head
