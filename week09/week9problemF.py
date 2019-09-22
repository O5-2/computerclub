from sys import stdin
n = int(stdin.readline())
A = sorted([int(i) for i in stdin.readline().split(' ')])

days = 0
for i in range(0, n):
    if A[i] > days:
        days += 1

print(days)
