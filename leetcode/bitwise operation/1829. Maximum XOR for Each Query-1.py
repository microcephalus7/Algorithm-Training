# 비트 연산
# 보충 필요

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        all_xor = 0
        result = []

        # 비트 이동 연산자로 최대값 만들기
        max_num = (1 << maximumBit) - 1

        for num in nums:
            all_xor ^= num

        while nums:
            # 1 to 3
            # 01 & 11 = 01
            # 01 ^ 11 = 10

            res = (all_xor & max_num) ^ max_num
            result.append(res)

            all_xor ^= nums.pop()

        return result
