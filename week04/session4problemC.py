from sys import stdin
h, m, s, t1, t2 = [int(i) for i in stdin.readline().split(' ')]

borders = sorted([5*h, m, s])
bool1a = (5*t1 <= borders[0]) or (borders[2] < 5*t1)
bool1b = (5*t2 <= borders[0]) or (borders[2] < 5*t2)
bool2a = (borders[0] < 5*t1) and (5*t1 <= borders[1])
bool2b = (borders[0] < 5*t2) and (5*t2 <= borders[1])
bool3a = (borders[1] < 5*t1) and (5*t1 <= borders[2])
bool3b = (borders[1] < 5*t2) and (5*t2 <= borders[2])

if (((bool1a and bool1b) or (bool2a and bool2b)) or (bool3a and bool3b)):
    print("YES")
else:
    print("NO")
