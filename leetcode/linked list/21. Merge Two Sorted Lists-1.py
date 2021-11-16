import collections
from typing import Deque, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        new_node = runner = None

        def collector(node: Optional[ListNode]):

            nonlocal values

            if node:
                values.append(node.val)
                collector(node.next)

        collector(l1)
        collector(l2)

        values.sort(reverse=True)

        while values:
            value = values.pop()
            runner = ListNode(value)
            runner = runner.next

        return new_node
