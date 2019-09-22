from sys import stdin
n, a, b = [int(i) for i in stdin.readline().split(' ')]
c = 0
sizes = [int(i) for i in stdin.readline().split(' ')]

denied = 0
for i in range(0, n):
    if (sizes[i] == 2) and (b > 0):
        b -= 1
    elif (sizes[i] == 1) and (a > 0):
        a -= 1
    elif (sizes[i] == 1) and (b > 0):
        c += 1
        b -= 1
    elif (sizes[i] == 1) and (c > 0):
        c -= 1
    else:
        denied += sizes[i]

print(denied)
