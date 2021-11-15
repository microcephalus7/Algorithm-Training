# 해시 테이블

# dictonary value, index 쌍의 해시테이블
# nums 돌며 target - num 이 dict 에 있으면 return

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            new_num = target - num
            if new_num in hash_map:
                return [index, hash_map[new_num]]
            hash_map[num] = index
