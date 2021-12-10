# 분류한 후 정렬

# 미리 분류 한 후 정렬 후 합체
# lambda
# 참고

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
