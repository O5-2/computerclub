from sys import stdin
from collections import defaultdict
q = int(stdin.readline())
for i in range(0, q):
    n = int(stdin.readline())
    sticks = [int(i) for i in stdin.readline().split(' ')]
    lengths = defaultdict(int)
    for j in sticks:
        lengths[j] += 1
    arranged = sorted(list(lengths.keys()))
    area = arranged[0]*arranged[-1]
    impossible = False
    for l in range(0, len(arranged)):
        if ((lengths[arranged[l]] % 2 == 1) or (arranged[l]*arranged[-l-1] != area)) or (lengths[arranged[l]] != lengths[arranged[-l-1]]):
            impossible = True
            break
    if not impossible:
        print("YES")
    else:
        print("NO")
