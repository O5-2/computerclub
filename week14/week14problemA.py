from sys import stdin
from collections import defaultdict
n = int(stdin.readline())
days = [int(i) for i in stdin.readline().split(' ')]

dp = defaultdict(lambda: 101) # Effectively sets non-initialized items to infinity.
dp[(-1, "r")] = 0 # Base case.
for i in range(0, n):
    dp[(i, "r")] = 1+min(dp[(i-1, "r")], dp[(i-1, "g")], dp[(i-1, "c")])
    if days[i] >= 2:
        dp[(i, "g")] = min(dp[(i-1, "r")], dp[(i-1, "c")])
    if days[i] % 2 == 1:
        dp[(i, "c")] = min(dp[(i-1, "r")], dp[(i-1, "g")])

print(min(dp[(n-1, "r")], dp[(n-1, "g")], dp[(n-1, "c")]))
# dp[(i, "x")] represents the minimum number of days you've rested at the end of the Ith day, where "x" is what you did that day.
