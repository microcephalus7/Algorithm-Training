# list 에서 k 개를 뽑은 것 에서 가장 큰 값과 가장 작은 값을 뺀 수가 가장 작은 값 찾기

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        min_dif = sys.maxsize

        nums.sort()

        for i in range(len(nums) - k + 1):
            sliced_num = nums[i:i+k]
            min_dif = min(min_dif, sliced_num[-1] - sliced_num[0])

        return min_dif
