from sys import stdin
n = int(stdin.readline())
likes = [int(i) for i in stdin.readline().split(' ')]

triangle = False
for i in range(0, n):
    if (likes[likes[likes[i]-1]-1]-1 == i):
        triangle = True
        break

if triangle:
    print("YES")
else:
    print("NO")
