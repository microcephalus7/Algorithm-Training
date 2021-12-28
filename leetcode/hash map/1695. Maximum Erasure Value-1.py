# subarray 에서 중복을 없앤 후 제일 큰 합
# 슬라이딩 윈도우, 해시 테이블
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        used = {}
        max_sum = start = 0

        for index, char in enumerate(nums):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_sum = max(max_sum, sum(nums[start:index + 1]))

            used[char] = index

        return max_sum
