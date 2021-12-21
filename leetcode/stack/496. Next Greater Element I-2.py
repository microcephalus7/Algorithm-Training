# 자신의 슈퍼셋인 리스트의 요소들이 자신의 그 다음 요소들 중에 자신보다 큰 요소 찾기
# stack, 해시 테이블, DP?
# 참고


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stack = []
        table = {}

        # nums2 를 먼저 해시 테이블 화 시킴
        for num in nums2:
            while stack and num > stack[-1]:
                table[stack.pop()] = num
            stack.append(num)

        # stack 에 남은 요소들 -1
        while stack:
            table[stack.pop()] = -1

        # num1 돌며 table 값 이용
        for num in nums1:
            result.append(table[num])

        return result
