# counter, stack

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = []
        res = 0
        arr_len = len(arr)

        dict = collections.Counter(arr)

        stack = sorted(dict.values())

        while arr_len > len(arr) // 2:
            value = stack.pop()
            arr_len -= value
            res += 1

        return res
