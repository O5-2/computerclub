# Leetcode problem: K Closest Points to Origin (973)

from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        from math import sqrt
        q = []
        for i in points:
            if len(q) < K:
                heapq.heappush(q, (-1*sqrt(i[0]**2 + i[1]**2), i))
                continue
            j = heapq.heappop(q)
            if sqrt(i[0]**2 + i[1]**2) <= -1*j[0]:
                heapq.heappush(q, (-1*sqrt(i[0]**2 + i[1]**2), i))
            else:
                heapq.heappush(q, j)
        ans = []
        while q:
            ans.append(heapq.heappop(q)[1])
        return ans

s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
