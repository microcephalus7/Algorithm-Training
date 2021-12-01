# list 변환, deque

# Definition for singly-linked list.
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values: Deque = collections.deque()

        if not head:
            return True

        while head is not None:
            values.append(head.val)
            head = head.next

        for i in range(len(values) // 2):
            left = values.popleft()
            right = values.pop()
            if left != right:
                return False

        return True
