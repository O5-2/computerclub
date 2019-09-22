# Leetcode problem: Coin Change (322)

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import defaultdict
        csum = defaultdict(lambda: -1)
        csum[0] = 0
        for i in range(1, amount+1):
            ans = -1
            for j in coins:
                if j <= i:
                    val = 1+csum[i-j]
                    if val == 0:
                        continue
                    if (val != 0) and (ans == -1):
                        ans = val
                    else:
                        ans = min(ans, val)
            csum[i] = ans
        return csum[amount]

s = Solution()
print(s.coinChange([1,2,5], 11)) # Returns 3. Correct.
print(s.coinChange([2], 3)) # Returns -1. Correct.
print(s.coinChange([1,2,5], 100)) # Returns 20. Correct.
print(s.coinChange([186,419,83,408], 6249)) # Returns 20. Correct.
