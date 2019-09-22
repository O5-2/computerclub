from sys import stdin
n = int(stdin.readline())
a = [int(i) for i in stdin.readline().split(' ')]

s = set(a)

if 0 in s:
    s.remove(0)
print(len(s))
