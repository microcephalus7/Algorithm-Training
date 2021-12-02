# defaultdict, sort, lambda

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = collections.defaultdict(lambda: -1)

        for index, value in enumerate(order):
            order_map[value] = index

        # index 를 sort 의 key 로 사용
        return ''.join(sorted(s, key=lambda x: order_map[x]))
