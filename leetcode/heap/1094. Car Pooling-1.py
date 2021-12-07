# heapq, while
# 연구 필요

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        heap = []

        for (count, where_from, where_to) in trips:

            while heap and heap[0][0] <= where_from:
                pop_count = heapq.heappop(heap)[1]
                capacity += pop_count

            if count > capacity:
                return False
            else:
                capacity -= count
                heapq.heappush(heap, (where_to, count))

        return True
