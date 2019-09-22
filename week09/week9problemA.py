from sys import stdin
n = int(stdin.readline())
trim = lambda s: s[:-1] if s[-1] == "\n" else s
moves = trim(stdin.readline())

x = 0
y = 0
for i in moves:
    if i == 'U':
        y += 1
    elif i == 'R':
        x += 1
    elif i == 'L':
        x -= 1
    elif i == 'D':
        y -= 1

print(len(moves)-abs(x)-abs(y))
