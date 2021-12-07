# 최소값 찾기
# for, max

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []

        min_dif = sys.maxsize

        arr.sort()

        for i in range(len(arr) - 1):
            min_dif = min(min_dif, abs(arr[i + 1] - arr[i]))

        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == min_dif:
                result.append([arr[i], arr[i+1]])

        return result
