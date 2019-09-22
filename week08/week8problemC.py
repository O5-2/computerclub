from sys import stdin
trim = lambda s: s[:-1] if s[-1] == "\n" else s
T = int(stdin.readline())

for i in range(0, T):
    n = int(stdin.readline())
    s = trim(stdin.readline())
    possible = True
    for j in range(0, n//2 + 1):
        if abs(ord(s[j])-ord(s[-(j+1)])) not in [0, 2]:
            possible = False
    if possible:
        print("YES")
    else:
        print("NO")
