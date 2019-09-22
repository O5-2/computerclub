from sys import stdin
s, v1, v2, t1, t2 = [int(i) for i in stdin.readline().split(' ')]

work1 = t1+(s*v1)+t1
work2 = t2+(s*v2)+t2

if work1 < work2:
    print("First")
elif work1 > work2:
    print("Second")
else:
    print("Friendship")
