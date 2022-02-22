# 가장 큰 합의 길이 K 의 subsequence 배열
# heapq
# heappushpop
# 참고

from heapq import heappush, heappushpop


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i, n in enumerate(nums):
            # 넣고 빼는 작업을 통해 최소값 날림
            if len(res) == k:
                heappushpop(res, (n, i))
            else:
                heappush(res, (n, i))

        # 순서 보전
        return [x[0] for x in sorted(res, key=lambda x: x[1])]
