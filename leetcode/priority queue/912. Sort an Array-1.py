# heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []

        for i in range(len(nums)):
            result.append(heapq.heappop(nums))

        return result
