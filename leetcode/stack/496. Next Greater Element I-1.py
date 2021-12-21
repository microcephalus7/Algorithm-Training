# 브루트 포스

# 실패
# 실패 이유
# nums1 을 먼저 이용해 반드시 nums2 를 접근해야 한다고 생각함
# nums2 를 이전에 풀었던 739 번을 이용하여 풀 생각 못 함
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)

        for num1_idx in range(len(nums1)):
            idx = nums2.index(nums1[num1_idx])

            for num2_idx in range(idx + 1, len(nums2)):
                if nums2[num2_idx] > nums1[num1_idx]:
                    ans[num1_idx] = nums2[num2_idx]

        return ans
