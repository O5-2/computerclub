from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    N = int(stdin.readline())
    A = [int(i) for i in stdin.readline().split(' ')]
    lowest = 100001
    lowestIndex = 0
    for j in range(len(A)-1, -1, -1):
        if A[j] <= lowest:
            lowest = A[j]
            lowestIndex = j
    print(lowestIndex+1)
