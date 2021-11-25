# sort
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if output and interval[0] <= output[-1][1]:
                output[-1][1] = max(interval[1], output[-1][1])
            else:
                output.append(interval)

        return output
