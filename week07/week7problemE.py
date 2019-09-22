from sys import stdin
n, m = [int(i) for i in stdin.readline().split(' ')]
A = [int(i) for i in stdin.readline().split(' ')]
B = [int(i) for i in stdin.readline().split(' ')]

dorm = 0
rooms = 0
for i in range(0, len(B)):
    while rooms+A[dorm] < B[i]:
        rooms += A[dorm]
        dorm += 1
    print(str(dorm+1) + " " + str(B[i]-rooms))
