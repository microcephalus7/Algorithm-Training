# List 의 페어 문자열이 특정 문자열과 같은지?
# 브루트 포스

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    result += 1

        return result
