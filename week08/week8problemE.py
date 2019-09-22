from sys import stdin
from math import sqrt
trim = lambda s: s[:-1] if s[-1] == "\n" else s
q = int(stdin.readline())

for i in range(0, q):
    n = int(stdin.readline())
    s = trim(stdin.readline())
    if len(s) % 2 == 1:
        print("YES")
        print(2)
        print(s[:(n-1)//2] + " " + s[(n-1)//2:])
    elif len(s) != 2:
        print("YES")
        print(2)
        print(s[:(n-2)//2] + " " + s[(n-2)//2:])
    elif s[0] < s[1]:
        print("YES")
        print(2)
        print(s[0] + " " + s[1])
    else:
        print("NO")



