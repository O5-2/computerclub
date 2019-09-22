# Leetcode problem: Number of Enclaves (1020)

from typing import List

class Solution:
    global seen
    seen = set()
    
    def traverseLand(self, A: List[List[int]], location: tuple) -> None:
        global seen
        s = Solution()
        if (A[location[0]][location[1]] == 0) or ((location[0], location[1]) in seen):
            return None
        seen.add(location)
        if (location[0] != 0):
            s.traverseLand(A, (location[0]-1, location[1]))
        if (location[0] != len(A)-1):
            s.traverseLand(A, (location[0]+1, location[1]))
        if (location[1] != 0):
            s.traverseLand(A, (location[0], location[1]-1))
        if (location[1] != len(A[0])-1):
            s.traverseLand(A, (location[0], location[1]+1))
    
    def numEnclaves(self, A: List[List[int]]) -> int:
        global seen
        seen = set()
        s = Solution()
        land = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 1:
                    land += 1
                if ((i in (0, len(A)-1)) or (j in (0, len(A[0])-1))) and (A[i][j] == 1):
                    s.traverseLand(A, (i, j))
        return land-len(seen)

s = Solution()
arrayA = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s.numEnclaves(arrayA))
arrayB = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(s.numEnclaves(arrayB))
