# 그래프 일정 재구성
# DFS
# 참고 코드
# 최적화

import collections
from typing import List


class Solution:
    # [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 생성
        graph = collections.defaultdict(list)

        # 그래프 순서대로 구성
        # JFK = [SFO, ATL]
        # SFO = [ATL]
        # ATL = [JFK, SFO]

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        result = []

        def dfs(a):

            result.append(a)

            while graph[a]:
                dfs(graph[a].pop())
            # result.append(a)

        dfs("JFK")

        return result
        # return result[::-1]
