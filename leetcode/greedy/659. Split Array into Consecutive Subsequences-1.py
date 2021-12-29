# 배열을 연속  시퀸스 sub-array 로 분할
# greedy
# 보충 필요
class Solution:
    # 1, 2, 3, 3, 4, 5
    # 1, 2, 3, 3, 4, 4, 5, 5
    # 1, 2, 3, 4, 4, 5
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = collections.Counter()

        for num in nums:
            if not left[num]:
                continue
            left[num] -= 1

            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num+2] -= 1
                end[num + 2] += 1
            else:
                return False

        return True
