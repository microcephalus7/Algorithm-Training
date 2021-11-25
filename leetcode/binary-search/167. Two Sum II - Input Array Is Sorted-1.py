# 투 포인터

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            combined_number = numbers[left] + numbers[right]
            if combined_number > target:
                right -= 1
            elif combined_number < target:
                left += 1
            else:
                return [left + 1, right + 1]
