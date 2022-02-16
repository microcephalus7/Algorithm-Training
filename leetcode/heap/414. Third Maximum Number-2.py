# 배열에서 중복을 거른 후 세번째로 큰 수
# heapq
# nlargest

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        if len(nums) > 2:
            return heapq.nlargest(3, nums)[-1]
        else:
            return heapq.nlargest(1, nums)[0]
