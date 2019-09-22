from sys import stdin
n, k = [int(i) for i in stdin.readline().split(' ')]
candyGains = [int(i) for i in stdin.readline().split(' ')]

stash = 0
candiesGiven = 0
for i in range(0, n):
    stash += candyGains[i]
    candiesGiven += min(8, stash)
    stash -= min(8, stash)
    if candiesGiven >= k:
        print(str(i+1))
        break
if candiesGiven < k:
    print("-1")
