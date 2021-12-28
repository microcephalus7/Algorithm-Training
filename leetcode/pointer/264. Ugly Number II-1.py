# 소수들이 2, 3, 5 인 n 번째 수 구하기

# 수를 나누는게 아님
# 2, 3, 5 로만 곱해진 수들 만들기
# 쓰리 포인터
# 보충 필요

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly_nums = [1]

        i2, i3, i5 = 0, 0, 0

        while n > 1:

            u2, u3, u5 = 2 * ugly_nums[i2], 3 * \
                ugly_nums[i3], 5 * ugly_nums[i5]

            umin = min((u2, u3, u5))

            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly_nums.append(umin)

            n -= 1

        return ugly_nums[-1]
