# 자료형 변환

# List(String 으로도 가능)
# 재귀 or stack

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 재귀
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     output = []

    #     def collector(node: ListNode):
    #         if node:
    #             output.append(node.val)
    #             collector(node.next)

    #     collector(head)

    #     return output == output[::-1]

    # stack
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     output = ""

    #     stack = [head]

    #     while stack:
    #         new_node = stack.pop()

    #         if new_node:
    #             output += str(new_node.val)
    #             stack.append(new_node.next)

    #     return output == output[::-1]

    # while
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        output = ""

        while head:
            output += str(head.val)
            head = head.next

        return output == output[::-1]
