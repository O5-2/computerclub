# Leetcode problem: Coin Change 2 (518)

from typing import List

class Solution:
    global waysOld
    from collections import defaultdict
    waysOld = defaultdict(lambda: 0)
    # waysOld[i][j] is the number of ways if the amount that gets subtracted from is j and you can only use coins up to index i inclusive.
    global ways
    ways = defaultdict(lambda: 0)
    # ways[i][j] is the number of ways if the amount that gets added to is i and the current smallest-coin limit is j.
    global a
    a = 0
    global c
    c = []
    
    def helperOld(self, amount: int, coins: List[int]) -> int:
        global waysOld
        s = Solution()
        if amount == 0:
            return 1
        ans = 0
        for i in range(0, len(coins)):
            if amount < coins[i]:
                break
            if (i, amount-coins[i]) in waysOld:
                ans += waysOld[(i, amount-coins[i])]
            else:
                ans += s.helperOld(amount-coins[i], coins[:i+1])
        return ans
    
    def changeOld(self, amount: int, coins: List[int]) -> int:
        global waysOld
        for i in range(0, len(coins)):
            waysOld[(i, 0)] = 1
        if len(coins) == 0:
            return int(amount == 0)
        s = Solution()
        coins.sort()
        for i in range(0, len(coins)):
            for j in range(1, amount+1):
                waysOld[(i, j)] = s.helperOld(j, coins[:i+1])
        return waysOld[(len(coins)-1, amount)]

    def helper(self, value: int, coin: int) -> int:
        global ways
        global a
        global c
        s = Solution()
        ans = 0
        if value+c[coin] == a:
            ways[(value, coin)] = 1
            return 1
        if value+c[coin] < a:
            if (value+c[coin], coin) in ways:
                ans += ways[(value+c[coin], coin)]
            else:
                ans += s.helper(value+c[coin], coin)
        if coin+1 < len(c):
            if (value, coin+1) in ways:
                ans += ways[(value, coin+1)]
            else:
                ans += s.helper(value, coin+1)
        ways[(value, coin)] = ans
        return ans

    def change(self, amount: int, coins: List[int]) -> int:
        global ways
        global a
        global c
        from collections import defaultdict
        ways = defaultdict(lambda: 0)
        for i in range(0, len(coins)):
            ways[(amount, i)] = 1
        a = amount
        c = sorted(coins)
        if len(coins) == 0:
            return int(amount == 0)
        if amount == 0:
            return 1
        s = Solution()
        ans = s.helper(0, 0)
        return ways[(0, 0)]

s = Solution()
print(s.changeOld(5, [1,2,5]))
print(s.changeOld(3, [2]))
print(s.changeOld(10, [10]))
# Does this run into a TLE if amount is really big?
print(s.changeOld(100, [1,2,5]))
print(s.changeOld(5000, [1,2,5]))
# No, but it does if amount *and* len(coins) are really big.

print(s.change(5, [1,2,5]))
print(s.change(3, [2]))
print(s.change(10, [10]))
#print(ways)
# Does this run into a TLE if amount is really big?
print(s.change(100, [1,2,5]))
print(s.change(5000, [1,2,5]))
# Maybe, maybe not. It looks cleaner, at any rate.
# Oh. It runs into a recursionDepth error.
# That's the fundamental problem: Depth can get up to 5000, and if it's, say, 5000 [1] then you're out of luck.
# Of course, actually trying that makes it work perfectly fine, so...

# Also: I still can't get the cross-check of ways to work. For whatever reason.
# It does run into a Time Limit Exceeded. Well, time to see what's wrong with the cross-check of ways.
# ... I can't make heads or tails of it. I'm lucky it works at all.
# Figured it out.

# ARGH FINALLY I DID IT
# todo tomorrow: clean this up a bit, maybe?
