# DP

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = collections.defaultdict(int)

        for i in nums:
            if dict[i] == 0:
                dict[i] = nums.count(i)

            if dict[i] > len(nums)//2:
                return i
