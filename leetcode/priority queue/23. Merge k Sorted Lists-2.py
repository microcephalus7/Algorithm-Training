# 여러 연결 리스트들 정렬된 하나의 연결 리스트로 만들기
# heapq, 반복

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        result = result_copy = ListNode()

        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next

        while heap:
            value = heapq.heappop(heap)
            result_copy.next = ListNode(value)
            result_copy = result_copy.next

        return result.next
