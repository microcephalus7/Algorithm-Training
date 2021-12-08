# 그리디
# deque

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = collections.deque(sorted(piles))
        result = 0
        for i in range(len(piles) // 3):
            piles.popleft()
            piles.pop()
            result += piles.pop()

        return result
