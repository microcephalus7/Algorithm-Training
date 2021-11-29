# 분할정복

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2

        # 분할
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # 정복
        return [b, a][nums.count(a) > half]
