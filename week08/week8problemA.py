from sys import stdin
trim = lambda s: s[:-1] if s[-1] == "\n" else s
s = trim(stdin.readline())
t = trim(stdin.readline())

possible = True
if len(s) != len(t):
    possible = False
else:
    for i in range(0, len(s)):
        if (s[i] in "aeiou") ^ (t[i] in "aeiou"):
            possible = False
            
if possible:
    print("Yes")
else:
    print("No")
