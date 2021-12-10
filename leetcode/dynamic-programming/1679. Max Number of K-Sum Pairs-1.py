# List 에서 한 쌍의 요소가 특정 수가 되는 최대 쌍 갯수
# 투 포인터

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        result = 0

        left, right = 0, len(nums) - 1

        while left < right:
            sum_pair = nums[left] + nums[right]

            if sum_pair < k:
                left += 1
            elif sum_pair > k:
                right -= 1
            else:
                result += 1
                left += 1
                right -= 1

        return result
