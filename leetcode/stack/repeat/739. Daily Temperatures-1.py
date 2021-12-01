class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):

            while stack and value > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = index - last

            stack.append(index)

        return answer
