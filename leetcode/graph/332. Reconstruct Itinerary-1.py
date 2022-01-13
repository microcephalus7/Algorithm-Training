# 그래프 일정 재구성
# DFS
# 참고 코드

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        result = []

        def dfs(a):

            while graph[a]:
                dfs(graph[a].pop(0))
            result.append(a)

        dfs("JFK")

        return result[::-1]
