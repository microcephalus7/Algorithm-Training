class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        nums_len = len(nums)

        return (nums[nums_len - 1] * nums[nums_len - 2]) - (nums[0] * nums[1])
