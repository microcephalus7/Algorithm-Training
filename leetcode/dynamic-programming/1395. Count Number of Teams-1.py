# 보충 필요

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ascend = descend = 0

        for index, value in enumerate(rating):
            llc = rgc = lgc = rlc = 0

            for l in rating[:index]:
                if l < value:
                    llc += 1
                if l > value:
                    lgc += 1

            for r in rating[index+1:]:
                if r > value:
                    rgc += 1
                if r < value:
                    rlc += 1

            ascend += llc * rgc
            descend += lgc * rlc

        return ascend + descend
