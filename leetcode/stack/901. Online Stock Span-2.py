# 리스트에서 요소 자신의 앞 요소 중에 작은 게 몇 개인가
# monotonic stack
# 캐싱을 stack 내부에서 함
# 참고

class StockSpanner:

    def __init__(self):
        self.monotone_stack = []

    # 100, 80, 60, 70, 60, 75, 85
    def next(self, price: int) -> int:
        # [(100, 1),(80, 1), (60, 1)]
        # [(100, 1), (80, 1), (70, 2)]
        # [(100, 1), (80, 1), (70, 2), (60, 1)]
        # [(100, 1), (80, 1), (75, 4)]
        # [(100, 1), (85, 6)]
        stack = self.monotone_stack

        cur_price_quote, cur_price_span = price, 1

        while stack and stack[-1][0] <= cur_price_quote:
            prev_price_quote, prev_price_span = stack.pop()

            cur_price_span += prev_price_span

        stack.append((cur_price_quote, cur_price_span))

        return cur_price_span
