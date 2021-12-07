# 이진검색
# bisect
# 최적화

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            expected = target - value

            nums = numbers[index + 1:]

            i = bisect.bisect_left(nums, expected)

            if i < len(nums) and numbers[i + index + 1] == expected:
                return index + 1, i + index + 2
