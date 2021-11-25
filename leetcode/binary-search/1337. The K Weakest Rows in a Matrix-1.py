class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        out = [[i, self.binary_search(arr)] for i, arr in enumerate(mat)]
        out.sort(key=lambda x: x[1])

        return [out[i][0] for i in range(k)]

    def binary_search(self, arr):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == 1:
                start = mid + 1
            else:
                end = mid - 1

        return start
