# 반복
# 이진 탐색
# 보충 필요
# 가치 있음

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        # 무게를 기준으로 이진 검색
        # 요소 중 가장 큰 수 left, 전부 다 합친 수 right
        left, right = max(weights), sum(weights)

        while left < right:

            # 중간 값
            mid = left + (right - left) // 2

            current = 0
            days = 1

            for w in weights:
                # 중간 보다 넘어갈 경우
                if current + w > mid:
                    # 날일 +1
                    days += 1
                    # 지금 무게 리셋
                    current = 0

                # 무게 더하기
                current += w

            # 날일수가 목표 날일 수 보다 클 경우
            if days > D:
                # 최소 무게를 중간 보다 1 높임
                left = mid + 1
            # 목표 수가 날이 보다 같거나 작을 경우
            else:
                # 최대 무게를 중간 값으로 생성
                right = mid

        return left
