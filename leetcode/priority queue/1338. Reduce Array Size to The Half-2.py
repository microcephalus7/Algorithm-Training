# counter, heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = []
        res = 0
        arr_len = len(arr)

        dict = collections.Counter(arr)

        for i in dict.values():
            heapq.heappush(heap, -i)

        while arr_len > len(arr) // 2:
            value = -heapq.heappop(heap)
            arr_len -= value
            res += 1

        return res
