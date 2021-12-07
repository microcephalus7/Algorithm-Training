# Counter, heapq

class Solution:
    def frequencySort(self, s: str) -> str:

        cnt = collections.Counter(s)

        heap = [(-count, value) for value, count in cnt.items()]
        heapq.heapify(heap)

        # Build string
        res = []
        while heap:
            count, value = heapq.heappop(heap)
            res += [value] * -count
        return ''.join(res)
