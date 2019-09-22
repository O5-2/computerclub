# Leetcode problem: Minimum Path Sum (64)

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        minSums = [[] for i in range(0, len(grid))]
        minSums[0].append(grid[0][0])
        for i in range(1, len(grid)):
            minSums[i].append(grid[i][0]+minSums[i-1][0])
        for i in range(1, len(grid[0])):
            minSums[0].append(grid[0][i]+minSums[0][i-1])
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                minSums[i].append(grid[i][j]+min(minSums[i-1][j], minSums[i][j-1]))
        return minSums[-1][-1]

s = Solution()
a = [[1,3,1],[1,5,1],[4,2,1]]
b = [[3,2,1,3],[1,9,2,3],[9,1,5,4]]
print(s.minPathSum(a))
print(s.minPathSum(b))
