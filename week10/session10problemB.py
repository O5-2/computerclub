# Leetcode problem: Max Area of Island (695)

from typing import List

class Solution:
    global seen
    seen = set()
    global maxSize
    maxSize = 0
    global size
    size = 0
    
    def areaOfIsland(self, grid: List[List[int]], start: tuple) -> None:
        global seen
        global size
        s = Solution()
        if (grid[start[0]][start[1]] == 0) or ((start[0], start[1]) in seen):
            return None
        seen.add(start)
        size += 1
        if (start[0] != 0):
            s.areaOfIsland(grid, (start[0]-1, start[1]))
        if (start[0] != len(grid)-1):
            s.areaOfIsland(grid, (start[0]+1, start[1]))
        if (start[1] != 0):
            s.areaOfIsland(grid, (start[0], start[1]-1))
        if (start[1] != len(grid[0])-1):
            s.areaOfIsland(grid, (start[0], start[1]+1))
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global seen
        global maxSize
        global size
        seen = set()
        maxSize = 0
        s = Solution()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if ((i, j) not in seen) and (grid[i][j] == 1):
                    size = 0
                    s.areaOfIsland(grid, (i, j))
                    maxSize = max(maxSize, size)
        return maxSize

s = Solution()
arrayA = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s.maxAreaOfIsland(arrayA))
arrayB = [[0,0,0,0,0,0,0,0]]
print(s.maxAreaOfIsland(arrayB))
