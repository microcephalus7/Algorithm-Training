class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: (abs(x[0] - 0) ** 2 + abs(x[1] - 0) ** 2))[:k]
