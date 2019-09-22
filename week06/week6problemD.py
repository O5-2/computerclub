from sys import stdin
n, m = [int(i) for i in stdin.readline().split(' ')]
trim = lambda s: s[:-1] if (s[-1] == "\n") else s
cells = []
for i in range(0, n):
    cells.append(trim(stdin.readline()))

possible = True
rightColumn = -1
bottomRow = -1
leftColumn = -1
topRow = -1
for i in range(0, m):
    if ("B" in [j[-(i+1)] for j in cells]):
        leftColumn = m-i-1
    if ("B" in [j[i] for j in cells]):
        rightColumn = i
for i in range(0, n):
    if ("B" in cells[i]):
        bottomRow = i
    if ("B" in cells[-(i+1)]):
        topRow = n-i-1
sidelength = max(rightColumn-leftColumn+1, bottomRow-topRow+1)
ans = sidelength**2
if (topRow == -1):
    ans = 1
if ((sidelength > n) or (sidelength > m)):
    possible = False
for i in range(topRow, bottomRow+1):
    for j in range(leftColumn, rightColumn+1):
        if cells[i][j] == "B":
            ans -= 1

if possible:
    print(ans)
else:
    print(-1)
