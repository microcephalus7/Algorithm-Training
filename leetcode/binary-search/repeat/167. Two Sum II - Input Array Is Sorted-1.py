# 이진 검색, 반복

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers) - 1):
            desired_number = target - numbers[i]

            left, right = i + 1, len(numbers) - 1

            while left <= right:
                mid = left + (right - left)//2

                if numbers[mid] < desired_number:
                    left = mid + 1
                elif numbers[mid] > desired_number:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]
