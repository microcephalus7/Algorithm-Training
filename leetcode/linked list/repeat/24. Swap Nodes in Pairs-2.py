# 페어 노드 스왑
# 노드 자체 스왑 (참조값 변경)
# 반복
# 실패
# 참조 값은 변경하는 순간 바뀜

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        copy = head

        while copy and copy.next:
            # 여기서 포인터를 잡더라도
            copy_next = copy.next
            # 여기서 바뀌기 때문에 의미 없음
            copy.next = copy.next.next
            # 무쓸모
            copy_next.next = copy

        return head
