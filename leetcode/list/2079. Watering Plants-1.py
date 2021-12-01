class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water_can = capacity
        steps = 0

        for i, v in enumerate(plants):
            steps += 1

            # 물 따르기

            water_can -= v

            # 다음 plant 보다 물 부족 시 물 채우기

            if i < len(plants) - 1 and water_can < plants[i + 1]:
                steps += 2 * (i + 1)
                water_can = capacity

        return steps
