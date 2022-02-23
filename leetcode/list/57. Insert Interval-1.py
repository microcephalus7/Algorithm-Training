# 인터벌 삽입
# list
# 반복, 정렬

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        for i in intervals:
            if result and result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result
