class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):

        top_max = []
        left_max = []
        for i in range(len(grid)):
            left_max.append(max(grid[i]))
        for i in range(len(grid[0])):
            top_max.append(max(item[i] for item in grid))
        result = 0
        for i in range(len(top_max)):
            for j in range(len(left_max)):
                if top_max[i] < left_max[j]:
                    result += top_max[i] - grid[i][j]
                else:
                    result += left_max[j] - grid[i][j]
        return result
