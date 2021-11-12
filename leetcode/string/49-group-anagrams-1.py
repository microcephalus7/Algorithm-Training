# defaultdict

# 논리
# defaultdict 생성
# for 문 돌며 정렬된 i 를 key 에 i append
# return values

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())
