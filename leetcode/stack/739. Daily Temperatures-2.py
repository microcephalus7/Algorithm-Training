# stack

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):

            while stack and value > stack[-1][1]:
                last_index, last_value = stack.pop()
                answer[last_index] = index - last_index

            stack.append((index, value))

        return answer
