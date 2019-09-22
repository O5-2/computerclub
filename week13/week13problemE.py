# Leetcode problem: Combination Sum IV (377)

from typing import List

class Solution:
    from collections import defaultdict
    csum = defaultdict(int)
    
    def helper(self, nums: List[int], target: int) -> int:
        global csum
        s = Solution()
        if target == 0:
            return 1
        ans = 0
        for i in nums:
            if i <= target:
                if target-i in csum:
                    ans += csum[target-i]
                else:
                    ans += s.helper(nums, target-i)
        csum[target] = ans
        return ans
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        global csum
        csum = defaultdict(int)
        s = Solution()
        return s.helper(nums, target)

s = Solution()
print(s.combinationSum4([1,2,3], 4))
print(s.combinationSum4([1], 4))
# todo: more test cases
