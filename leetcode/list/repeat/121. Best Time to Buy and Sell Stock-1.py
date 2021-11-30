# for, max, min

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0

        for i in prices:
            max_profit = max(max_profit, i - min_price)
            min_price = min(min_price, i)

        return max_profit
