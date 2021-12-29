# 배열을 연속  시퀸스 sub-array 로 분할
# heapq
# 보충 필요
class Solution:
    # 1, 2, 3, 3, 4, 5
    # 1, 2, 3, 3, 4, 4, 5, 5
    # 1, 2, 3, 4, 4, 5
    def isPossible(self, nums: List[int]) -> bool:

        tails = defaultdict(list)

        for num in nums:
            if tails[num - 1]:
                heappush(tails[num], heappop(tails[num-1]) + 1)
            else:
                heappush(tails[num], 1)

        return all(i >= 3 for tail in tails.values() for i in tail)
