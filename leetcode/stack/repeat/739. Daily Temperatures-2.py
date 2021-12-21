# 리스트의 요소의 앞에 더 높은 숫자가 몇번째 앞에 있는지
# stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):

            while stack and value > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = index - last

            stack.append(index)

        return result
