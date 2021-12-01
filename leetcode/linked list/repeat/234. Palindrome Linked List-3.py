# 런너, stack
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow = fast = head

        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow, fast = slow.next, fast.next.next

        if fast:
            slow = slow.next

        while slow is not None:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True
