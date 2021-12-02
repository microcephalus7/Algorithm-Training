# counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        dict = collections.Counter(stones)

        for i in jewels:
            result += dict[i]

        return result
