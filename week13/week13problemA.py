# Leetcode problem: Fibonacci Number (509)

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        prev = 0
        cur = 1
        for i in range(1, N):
            prev, cur = cur, prev+cur
        return cur

s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
