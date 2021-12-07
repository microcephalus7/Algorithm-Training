# 이진 검색 모듈, bisect
# 이진 검색 기본

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index

        else:
            return -1
