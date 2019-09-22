# Leetcode problem: Friend Circles (547)

from typing import List

class Solution:
    global seen
    seen = set()

    def traverseCircle(self, M: List[List[int]], i: int) -> None:
        global seen
        s = Solution()
        if i in seen:
            return None
        seen.add(i)
        for j in range(0, len(M)):
            if M[i][j] == 1:
                s.traverseCircle(M, j)
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        global seen
        seen = set()
        circles = 0
        s = Solution()
        for i in range(0, len(M)):
            if i not in seen:
                s.traverseCircle(M, i)
                circles += 1
        return circles

s = Solution()
arrayA = [[1,1,0],[1,1,0],[0,0,1]]
print(s.findCircleNum(arrayA))
arrayB = [[1,1,0],[1,1,1],[0,1,1]]
print(s.findCircleNum(arrayB))
