# Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map = collections.Counter(stones)
        res = 0

        for jewel in jewels:
            res += hash_map[jewel]

        return res
