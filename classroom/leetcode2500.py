class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
        # print(grid)
        result = 0
        for i in range(len(grid[0])):
            maxval = 0
            for j in grid:
                maxval = max(maxval, j[i])
            result += maxval
        return result
