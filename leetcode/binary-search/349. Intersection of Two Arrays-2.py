# 브루트 포스

from typing import Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set([])

        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)

        return list(result)
