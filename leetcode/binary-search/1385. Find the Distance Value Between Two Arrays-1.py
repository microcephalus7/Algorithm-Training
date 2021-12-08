# bisect
# 보충 필요

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()

        result = 0

        for element in arr1:

            left = bisect.bisect_left(arr2, element - d)
            right = bisect.bisect_right(arr2, element + d)

            if left == right:

                result += 1

        return result
