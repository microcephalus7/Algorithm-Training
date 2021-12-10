# subArray 의 합이 특정 수와 같은 것의 갯수 찾기
# DP
# 메모이제이션
# 보충 필요

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sum = 0

        running_sum = collections.defaultdict(int)
        running_sum[0] = 1

        for num in nums:
            sum += num

            result += running_sum[sum-k]

            running_sum[sum] += 1

        return result
