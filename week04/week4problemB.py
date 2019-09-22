# Leetcode problem: Sqrt(x) (69)

from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        mid = (left+right)//2
        while (left+1 < right):
            if (mid*mid < x):
                left = mid
            else:
                right = mid
            mid = (left+right)//2
        if (left+1)**2 == x:
            left += 1
        return left

s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
