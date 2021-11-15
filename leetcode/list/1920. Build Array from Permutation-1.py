class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            # nums[nums[i]] 집어넣기
            result.append(nums[nums[i]])

        return result
