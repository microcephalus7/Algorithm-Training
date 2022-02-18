from curses.ascii import SO
import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))

        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return str(heapq.heappop(nums))


solution = Solution()
print(solution.kthLargestNumber(["2", "21", "12", "1"], 3))
