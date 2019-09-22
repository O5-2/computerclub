# Leetcode problem: First Bad Version (278)

from typing import List

def isBadVersion(n):
    versions = ["N/A", False, False, False, True, True]
    return versions[n]

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n+1
        mid = (left+right)//2
        while (left+1 < right):
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid
            mid = (left+right)//2
        return left+1

s = Solution()
print(s.firstBadVersion(5))
