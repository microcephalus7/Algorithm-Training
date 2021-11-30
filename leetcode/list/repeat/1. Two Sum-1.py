# dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = collections.defaultdict(int)

        for index, num in enumerate(nums):
            desired_number = target - num
            if desired_number in dict:
                return [index, dict[desired_number]]
            else:
                dict[num] = index
