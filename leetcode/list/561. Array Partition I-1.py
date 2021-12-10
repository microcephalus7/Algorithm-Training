# 배열에서 n 개의 페어를 이용하여 min(a, b) 의 합으로 만들 수 있는 가장 큰 수
# 파이썬 다운

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
