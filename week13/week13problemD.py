# Leetcode problem: Unique Paths (64)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))

s = Solution()
print(s.uniquePaths(3, 2))
print(s.uniquePaths(7, 3))
print(s.uniquePaths(1, 6))
print(s.uniquePaths(1, 1))
print(s.uniquePaths(2, 5))
print(s.uniquePaths(2, 2))
