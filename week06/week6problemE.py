from sys import stdin
a, b, c, d = [int(i) for i in stdin.readline().split(' ')]
x, y, z = sorted([a, b, c])

print(max(d-y+x, 0)+max(d-z+y, 0))
