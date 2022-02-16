# 배열에서 중복을 거른 후 세번째로 큰 수
# list
# set

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        if len(nums) > 2:
            return nums[len(nums) - 3]
        else:
            return nums[-1]
