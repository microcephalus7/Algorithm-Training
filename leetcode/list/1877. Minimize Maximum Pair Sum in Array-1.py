# 작은 것과 큰 것 묶기

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res = []

        left = 0
        right = len(nums) - 1

        nums.sort()

        while left < right:
            res.append(nums[left] + nums[right])

            left += 1
            right -= 1

        return max(res)
