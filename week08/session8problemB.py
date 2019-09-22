from sys import stdin
n = int(stdin.readline())
A = [int(i) for i in stdin.readline().split(' ')]

left = 0
right = len(A)-1
points = {0: 0, 1: 0}
turn = 0
while left <= right:
    if A[right] >= A[left]:
        points[turn] += A[right]
        right -= 1
    else:
        points[turn] += A[left]
        left += 1
    turn = turn ^ 1

print(str(points[0]) + " " + str(points[1]))
