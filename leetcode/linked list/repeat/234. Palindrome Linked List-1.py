# list 변환

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        if not head:
            return True

        while head is not None:
            values.append(head.val)
            head = head.next

        return values == values[::-1]
