from sys import stdin
n, m = [int(i) for i in stdin.readline().split(' ')]
space = []
for i in range(0, n):
    space.append(stdin.readline()+"")

rightOnes = []
for i in range(0, n):
    curR = []
    for j in range(0, m):
        for k in range(j, m):
            if space[i][k] == "1":
                curR.append(k)
                break
        if len(curR) != j+1:
            curR.append(m)
    rightOnes.append(curR)
maxP = 0
for i in range(0, n):
    for j in range(0, m):
        perimeter = 0
        sideTop = m-j
        for leftSize in range(1, n-i+1):
            if space[i+leftSize-1][j] == "1":
                break
            sideTop = min(sideTop, rightOnes[i+leftSize-1][j]-j)
            perimeter = max(perimeter, 2*(sideTop+leftSize))
            leftSize += 1
        maxP = max(maxP, perimeter)

print(maxP)
