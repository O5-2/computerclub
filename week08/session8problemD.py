from sys import stdin
n = int(stdin.readline())
A = [int(i) for i in stdin.readline().split(' ')]

m = 1
c = 1
for i in range(1, n):
    if A[i] > A[i-1]:
        c += 1
        m = max(m, c)
    else:
        c = 1

print(m)
