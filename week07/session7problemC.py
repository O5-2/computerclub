# Leetcode problem: Remove Duplicates from Sorted Array (26)
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        if len(nums) != 1:
            for i in range(0, len(nums)):
                if nums[i] != nums[n]:
                    nums.insert(n+1, nums[i])
                    del nums[n+2]
                    n += 1
        return n+1

s = Solution()
nums = [1, 1, 2]
print(s.removeDuplicates(nums))
print(nums)
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))
print(nums)
nums = [1]
print(s.removeDuplicates(nums))
print(nums)
