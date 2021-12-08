# 반복, 함수
# 이진 탐색
# 보충 필요
# 최적화

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        if len(weights) == days:
            return left

        def isPossible(maxWeight):
            day, sums = 1, 0
            for weight in weights:
                sums += weight
                if sums > maxWeight:
                    day += 1
                    sums = weight
            return day <= days

        while left <= right:
            mid = (left+right)//2
            if isPossible(mid):
                result = mid
                right = mid-1
            else:
                left = mid+1

        return result
