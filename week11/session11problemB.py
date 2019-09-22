# Leetcode problem: Powerful Integers (970)

from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        s = set()
        for i in range(0, 20):
            for j in range(0, 20):
                if x**i + y**j <= bound:
                    s.add(x**i + y**j)
        return list(s)

s = Solution()
print(s.powerfulIntegers(2, 3, 10))
print(s.powerfulIntegers(3, 5, 15))
