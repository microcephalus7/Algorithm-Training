# 재귀

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recur(left: int, right: int) -> int:
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return recur(mid + 1, right)
                elif nums[mid] > target:
                    return recur(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return recur(0, len(nums) - 1)
