# 그래프 일정 재구성
# 반복
# 참고 코드
# 최적화

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 생성
        graph = collections.defaultdict(list)

        # 그래프 순서대로 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route, stack = [], ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]
