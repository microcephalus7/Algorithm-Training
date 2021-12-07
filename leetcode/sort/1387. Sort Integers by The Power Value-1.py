class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def sorter(num):
            count = 0

            while num != 1:

                if num % 2 == 0:
                    num /= 2
                else:
                    num = 3 * num + 1

                count += 1

            return count

        return sorted(range(lo, hi+1), key=lambda x: (sorter(x), int(x)))[k-1]


solution = Solution()
print(solution.getKth(7, 11, 4))
