from sys import stdin
n = int(stdin.readline())
A = [int(i) for i in stdin.readline().split(' ')]

d = {1: [], 2: [], 3: []}
for i in range(0, n):
    d[A[i]] = d[A[i]] + [i+1]

print(min(len(d[1]), len(d[2]), len(d[3])))
for i in range(0, min(len(d[1]), len(d[2]), len(d[3]))):
    print(str(d[1][i]) + " " + str(d[2][i]) + " " + str(d[3][i]))
