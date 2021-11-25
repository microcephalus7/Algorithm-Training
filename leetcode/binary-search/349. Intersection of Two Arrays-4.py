# 투포인터

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums1.sort()
        nums2.sort()

        i = j = 0

        while i < len(nums1) and j < len(nums2):
            pass
