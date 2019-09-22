from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    box = [int(x) for x in stdin.readline().split(' ')]
    N = len(box)-1
    Ns = 0
    Nlocation = 0
    for j in range(0, len(box)):
        if box[j] == N:
            Ns += 1
            Nlocation = j
    if Ns == 1:
        if max(box) != N:
            print(max(box))
        else:
            print(max(box[:Nlocation]+box[Nlocation+1:]))
    else:
        print(max(box))
