from sys import stdin
from collections import defaultdict
n = int(stdin.readline())

dp = defaultdict(int)
for i in range(0, n):
    cur = [int(i) for i in stdin.readline().split(' ')]
    dp[(i, "a")] = cur[0]+max(dp[(i-1, "b")], dp[(i-1, "c")])
    dp[(i, "b")] = cur[1]+max(dp[(i-1, "a")], dp[(i-1, "c")])
    dp[(i, "c")] = cur[2]+max(dp[(i-1, "a")], dp[(i-1, "b")])

print(max(dp[(n-1, "a")], dp[(n-1, "b")], dp[(n-1, "c")]))
