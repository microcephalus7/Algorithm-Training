# dfs
# 보충 필요

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for i in elements:
                next_elements = elements[:]
                next_elements.remove(i)

                prev_elements.append(i)
                dfs(next_elements)

                prev_elements.pop()

        dfs(nums)

        return result
