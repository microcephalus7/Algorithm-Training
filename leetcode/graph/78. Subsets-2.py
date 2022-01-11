# 부분집합
# 파이썬스러운

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for i in range(len(result)):
                result.append(result[i] + [num])

        return result
