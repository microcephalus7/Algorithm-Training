# defaultdict, sort

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)

        for str in strs:
            dict[''.join(sorted(str))].append(str)

        return dict.values()
