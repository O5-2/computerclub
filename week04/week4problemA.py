# Leetcode problem: Capacity To Ship Packages Within D Days (1011)

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        s = sum(weights)
        left = 0
        right = s+1
        mid = (left+right)//2
        while (left+1 < right):
            j = 0
            possible = False
            for i in range(0, D):
                n = 0
                while (j < len(weights)) and (n+weights[j] <= mid):
                    n += weights[j]
                    j += 1
                if (j >= len(weights)):
                    possible = True
            if not possible:
                left = mid
            else:
                right = mid
            mid = (left+right)//2
        return left+1

s = Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(s.shipWithinDays([3,2,2,4,1,4], 3))
print(s.shipWithinDays([1,2,3,1,1], 4))
