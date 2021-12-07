# 이진검색
# bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            desired = target - value

            i = bisect.bisect_left(numbers[index + 1:], desired)

            if i < len(numbers[index + 1:]) and numbers[i + index + 1] == desired:
                return index + 1, i + index + 2
