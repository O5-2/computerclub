from sys import stdin
from collections import defaultdict
n, w = [int(i) for i in stdin.readline().split(' ')]
weights = []
values = []
for i in range(0, n):
    cur = [int(i) for i in stdin.readline().split(' ')]
    weights.append(cur[0])
    values.append(cur[1])

dp = defaultdict(lambda: defaultdict(int))
dp[0][0] = 0
for minInd in range(0, n):
    for allowed in range(0, w):
        dp[minInd+1][allowed] = max(dp[minInd+1][allowed], dp[minInd][allowed])
        if allowed+weights[minInd] <= w:
            dp[minInd+1][allowed+weights[minInd]] = max(dp[minInd+1][allowed+weights[minInd]], dp[minInd][allowed]+values[minInd])

print(max(dp[n].values()))

# This gets a TLE. An attempt to redo it in Kotlin is ongoing.
