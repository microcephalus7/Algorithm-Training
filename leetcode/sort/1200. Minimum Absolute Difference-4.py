# 최솟값 찾기

# clear

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []

        arr.sort()

        min_difference = arr[-1]

        for i in range(len(arr)-1):

            diff = abs(arr[i] - arr[i+1])

            if diff < min_difference:
                min_difference = diff
                result.clear()
                result.append([arr[i], arr[i+1]])

            elif diff == min_difference:
                result.append([arr[i], arr[i+1]])

        return result
