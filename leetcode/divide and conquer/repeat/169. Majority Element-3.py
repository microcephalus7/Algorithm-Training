# 과반수 찾기
# 분할 정복, 재귀

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

        # 백 트래킹 (정복)
        return [b, a][nums.count(a) > half]
