# 분리

# 논리
# isalpha 로 문자열, 숫자열 분리
# sort 로 정렬

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for i in logs:
            if i.split()[1].isalpha():
                letters.append(i)
            else:
                digits.append(i)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
