from sys import stdin
T = int(stdin.readline())

for i in range(0, T):
    n = int(stdin.readline())
    A = sorted([int(i) for i in stdin.readline().split(' ')])
    if len(A) < 3:
        print(0)
        continue
    print(min(len(A)-2, A[-2]-1))
