# list 에서 세 수의 합이 특정 수와 가장 가까울 시 세 수의 합
# 투 포인터, heapq

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        heap = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                heapq.heappush(heap, (abs(target - sum), sum))

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return heapq.heappop(heap)[1]
