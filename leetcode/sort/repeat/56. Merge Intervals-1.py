# sort

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort(key=lambda x: x[0])

        for i in intervals:
            if result and result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result
