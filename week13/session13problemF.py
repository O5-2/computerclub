from sys import stdin
from collections import defaultdict
trim = lambda s: s[:-1] if s[-1] == "\n" else s
s = trim(stdin.readline())
t = trim(stdin.readline())

dp = defaultdict(lambda: defaultdict(int))
dp[0][0] = 0
for minS in range(0, len(s)):
    for minT in range(0, len(t)):
        dp[minS+1][minT] = max(dp[minS+1][minT], dp[minS][minT])
        dp[minS][minT+1] = max(dp[minS][minT+1], dp[minS][minT])
        if s[minS] == t[minT]:
            dp[minS+1][minT+1] = max(dp[minS+1][minT+1], dp[minS][minT]+1)
            
edgesS = list(dp[len(s)].values())
edgesT = [dp[i][len(t)] for i in range(0, len(s)+1)]
ind = (-1, -1)
ans = ''
if max(edgesS) >= max(edgesT):
    for i in range(0, len(t)+1):
        if dp[len(s)][i] == max(edgesS):
            ind = (len(s), i)
            break
    while (ind[0] != 0) and (ind[1] != 0):
        cur = max(dp[ind[0]-1][ind[1]-1], dp[ind[0]-1][ind[1]], dp[ind[0]][ind[1]-1])
        if (cur == dp[ind[0]-1][ind[1]-1]) and (s[ind[0]-1] == t[ind[1]-1]):
            ind = (ind[0]-1, ind[1]-1)
            ans += s[ind[0]]
        elif cur == dp[ind[0]-1][ind[1]]:
            ind = (ind[0]-1, ind[1])
        else:
            ind = (ind[0], ind[1]-1)
else:
    for i in range(0, len(s)+1):
        if dp[i][len(t)] == max(edgesT):
            ind = (i, len(t))
            break
    while (ind[0] != 0) and (ind[1] != 0):
        cur = max(dp[ind[0]-1][ind[1]-1], dp[ind[0]-1][ind[1]], dp[ind[0]][ind[1]-1])
        if cur == dp[ind[0]-1][ind[1]-1]:
            ind = (ind[0]-1, ind[1]-1)
            ans += s[ind[0]]
        elif cur == dp[ind[0]-1][ind[1]]:
            ind = (ind[0]-1, ind[1])
        else:
            ind = (ind[0], ind[1]-1)
print(ans[::-1])
