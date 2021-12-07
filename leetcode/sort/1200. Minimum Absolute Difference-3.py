# 최솟값 찾기
# 파이썬 다운
# 캐시

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = sys.maxsize

        dict = collections.defaultdict(list)

        arr.sort()

        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            dict[diff].append([arr[i], arr[i+1]])

            min_diff = min(min_diff, diff)

        return dict[min_diff]
