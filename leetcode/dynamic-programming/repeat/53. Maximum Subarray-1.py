# subArray 의 합이 최대인 값 찾기
# 타뷸레이션
# for, max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        sum = 0

        for i in nums:

            if sum < 0:
                sum = 0

            sum += i
            max_sum = max(max_sum, sum)

        return max_sum
