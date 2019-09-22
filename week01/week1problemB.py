from sys import stdin
from collections import defaultdict

T = int(stdin.readline())

for i in range(0, T):
    N = int(stdin.readline())
    sticks = [int(i) for i in stdin.readline().split(' ')]
    maxArea = -1
    maxLength = -1
    secondMaxLength = -1
    df = lambda: 0
    dd = defaultdict(df)
    for i in sticks:
        dd[i] += 1
    for i in dd:
        if dd[i] >= 4:
            if i > maxLength:
                secondMaxLength = i
                maxLength = i
            elif i > secondMaxLength:
                secondMaxLength = i
        elif dd[i] >= 2:
            if i > maxLength:
                secondMaxLength = maxLength
                maxLength = i
            elif i > secondMaxLength:
                secondMaxLength = i
    maxArea = max(maxArea, maxLength*secondMaxLength)
    if secondMaxLength == -1:
        print(-1)
    else:
        print(maxArea)
