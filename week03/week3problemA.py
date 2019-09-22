# Leetcode problem: Binary Search (704)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left+right)//2
        while (left+1 < right):
            if (nums[mid] < target):
                left = mid
            elif (nums[mid] > target):
                right = mid
            else:
                return mid
            mid = (left+right)//2
        if (nums[left] == target):
            return left
        return -1

s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))
