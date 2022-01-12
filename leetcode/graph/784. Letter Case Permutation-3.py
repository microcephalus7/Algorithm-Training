# 대소문자 순열 (분화)
# 반복문, 파이썬스러운
# swapcase

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for ch in s:
            res = [x + cc for x in res for cc in {ch, ch.swapcase()}]
        return res
