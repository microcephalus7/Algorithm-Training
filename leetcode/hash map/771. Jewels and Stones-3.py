# defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.defaultdict(int)
        count = 0

        for i in stones:
            if i in jewels:
                freq[i] += 1

        for i in freq:
            count += freq[i]

        return count
