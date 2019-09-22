from sys import stdin
n, m = [int(i) for i in stdin.readline().split(' ')]
best = 101.0
for i in range(0, n):
    A = [int(i) for i in stdin.readline().split(' ')]
    best = min(best, A[0]/A[1])

print(best*m)
