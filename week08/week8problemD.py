from sys import stdin
trim = lambda s: s[:-1] if s[-1] == "\n" else s
s = trim(stdin.readline())
t = trim(stdin.readline())

i = 0
while ((i < len(s)) and (i < len(t))) and (s[-1-i] == t[-1-i]):
    i += 1

print(len(s) + len(t) - 2*i)
