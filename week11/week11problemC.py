# Leetcode problem: Shortest Bridge (934)

from typing import List

class Solution:
    def neighbors(self, A: List[List[int]], location: tuple) -> List[tuple]:
        ans = []
        if (location[0] != 0):
            ans.append((location[0]-1, location[1]))
        if (location[0] != len(A)-1):
            ans.append((location[0]+1, location[1]))
        if (location[1] != 0):
            ans.append((location[0], location[1]-1))
        if (location[1] != len(A[0])-1):
            ans.append((location[0], location[1]+1))
        return ans
    
    def shortestBridge(self, A: List[List[int]]) -> int:
        s = Solution()
        doneA = False
        start = (0, 0)
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 1:
                    start = (i, j)
                    doneA = True
                    break
            if doneA:
                break
        seenA = set([start])
        locations = [start]
        while locations:
            i = locations.pop(0)
            for j in s.neighbors(A, i):
                if (A[j[0]][j[1]] == 1) and (j not in seenA):
                    seenA.add(j)
                    locations.append(j)
        minLength = 197
        for i in seenA:
            locations = []
            seenL = set()
            for j in s.neighbors(A, (i[0], i[1])):
                if A[j[0]][j[1]] == 0:
                    locations.append((j[0], j[1], 1))
            while locations:
                j = locations.pop(0)
                if (j[:2] in seenL) or (j[2] >= minLength):
                    continue
                for k in s.neighbors(A, (j[0], j[1])):
                    if A[k[0]][k[1]] == 0:
                        locations.append((k[0], k[1], j[2]+1))
                    elif (k[0], k[1]) not in seenA:
                        minLength = min(minLength, j[2])
                seenL.add(j[:2])
        return minLength

s = Solution()
print(s.shortestBridge([[0,1],[1,0]]))
print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
