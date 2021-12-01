# 재귀, 실패
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list1_head = list1

        def recur(node: ListNode, index: int):
            # 앞에꺼 붙이기
            if index == a - 1:
                pass
            # 뒤에꺼 붙이기
            pass

        recur(list1, 0)

        return list1_head
