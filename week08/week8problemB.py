from sys import stdin
trim = lambda s: s[:-1] if s[-1] == "\n" else s
n = int(stdin.readline())
s = trim(stdin.readline())

if n >= 27:
    print(-1)
else:
    print(n-len(set(s)))
