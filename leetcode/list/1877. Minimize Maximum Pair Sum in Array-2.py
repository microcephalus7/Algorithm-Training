# 작은 것과 큰 것 묶기

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        result = 0

        left = 0
        right = len(nums) - 1

        nums.sort()

        while left < right:
            result = max(result, nums[left] + nums[right])

            left += 1
            right -= 1

        return result
