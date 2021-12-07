# 재귀
# 이진 검색 기본

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dfs(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return dfs(mid + 1, right)
                elif nums[mid] > target:
                    return dfs(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return dfs(0, len(nums) - 1)
