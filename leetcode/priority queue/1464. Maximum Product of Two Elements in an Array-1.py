# heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 1
        heap = []

        for i in nums:
            heapq.heappush(heap, -i)

        for i in range(2):
            res *= -(heapq.heappop(heap)) - 1

        return res
