# Leetcode problem: Merge Sorted Array (88)
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        for j in range(0, len(nums2)):
            while ((i < len(nums1)) and (nums1[i] < nums2[j])) and (i < m+j):
                i += 1
            nums1.insert(i, nums2[j])
            i += 1
        del nums1[n+m:]

s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
s.merge(nums1, 3, nums2, 3)
print(nums1)
print(nums2)
nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums2 = [1, 2, 2]
s.merge(nums1, 6, nums2, 3)
print(nums1)
print(nums2)
