class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [index for index, value in enumerate(sorted(nums)) if value == target]
