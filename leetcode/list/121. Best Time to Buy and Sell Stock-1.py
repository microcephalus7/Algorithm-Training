class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0

        # for 돌며 확인
        for i in prices:
            max_profit = max(max_profit, i - min_price)
            min_price = min(min_price, i)

        return max_profit
