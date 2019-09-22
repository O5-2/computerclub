from sys import stdin
n, m = [int(i) for i in stdin.readline().split(' ')]
trim = lambda s: s[:-1] if (s[-1] == "\n") else s
s = trim(stdin.readline())
t = trim(stdin.readline())

minNumber = n
minPlaces = [str(i) for i in range(1, n+1)]
for i in range(0, m-n+1):
    curNumber = 0
    curPlaces = []
    for j in range(0, n):
        if (s[j] != t[i+j]):
            curNumber += 1
            curPlaces.append(str(j+1))
    if (curNumber <= minNumber):
        minNumber = curNumber
        minPlaces = curPlaces

print(minNumber)
print(' '.join(minPlaces))
