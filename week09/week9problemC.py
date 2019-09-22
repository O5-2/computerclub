from sys import stdin
n = int(stdin.readline())
trees = []
for i in range(0, n):
    trees.append(int(stdin.readline()))
trees.append(10001)

time = 0
height = 0
for i in range(0, n):
    time += trees[i]-height+1
    height = trees[i]
    time += max(0, height-trees[i+1])+1
    height = min(height, trees[i+1])

print(time-1)
