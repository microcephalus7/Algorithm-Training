# defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        dict = collections.defaultdict(int)

        for i in stones:
            dict[i] += 1

        for i in jewels:
            result += dict[i]

        return result
