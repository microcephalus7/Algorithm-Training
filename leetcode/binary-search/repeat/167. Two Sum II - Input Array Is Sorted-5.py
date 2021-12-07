# 이진검색
# bisect
# 기능 사용

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            expected = target - value

            i = bisect.bisect_left(numbers, expected, index + 1)

            if i < len(numbers) and numbers[i] == expected:
                return index + 1, i + 1
