# 과반수 찾기
# 브루트 포스, DP
# defaultdict, for
# 최적화

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num
