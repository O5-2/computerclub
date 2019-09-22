# Leetcode problem: Climbing Stairs (70)

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1
        for i in range(1, n):
            prev, cur = cur, prev+cur
        return cur

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
