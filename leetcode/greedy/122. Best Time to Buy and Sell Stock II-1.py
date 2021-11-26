# greedy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        earn = 0
        buyed_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > buyed_price:
                earn += prices[i] - buyed_price

            buyed_price = prices[i]

        return earn
