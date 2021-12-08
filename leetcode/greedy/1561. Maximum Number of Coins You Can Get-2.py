# 파이썬 다운

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3:: 2])
