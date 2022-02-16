# Wiggle Sort
# list
# 배열 변환

class Solution:
    # [1, 1, 2, 2, 3, 3]
    # [1, 3, 1, 3, 2, 2]
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = len(nums[::2])

        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
