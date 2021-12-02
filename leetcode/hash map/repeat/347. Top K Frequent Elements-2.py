# counter, heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for i in freqs:
            heapq.heappush(freqs_heap, (-freqs[i], i))

        topk = []

        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
