# 리스트에서 요소 자신의 앞 요소 중에 작은 게 몇 개인가
# stack, 캐시
# 실패
# stack 캐싱 어떻게 해야할 지 답이 잘 안 나옴

class StockSpanner:

    def __init__(self):
        self.prices = []
        self.table = {}
        self.count = 0

    def next(self, price: int) -> int:
        result = 1

        stack = self.prices[:]

        while stack and stack[-1] <= price:
            result += 1
            stack.pop()

        self.table[self.count] = result
        self.count += 1
        self.prices.append(price)

        return result

        # Your StockSpanner object will be instantiated and called as such:
        # obj = StockSpanner()
        # param_1 = obj.next(price)
