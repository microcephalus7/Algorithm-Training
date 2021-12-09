# subArray 의 합이 최대인 값 찾기
# 메모이제이션
# for

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

        return max(nums)
