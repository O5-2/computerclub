# Leetcode problem: Peak Index in a Mountain Array (852)

from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A)
        mid = (left+right)//2
        while (left+1 < right):
            if (A[mid] < A[mid+1]):
                left = mid
            elif (A[mid-1] > A[mid]):
                right = mid
            else:
                return mid
            mid = (left+right)//2
        return left

s = Solution()
print(s.peakIndexInMountainArray([0, 1, 0]))
print(s.peakIndexInMountainArray([0, 2, 1, 0]))
