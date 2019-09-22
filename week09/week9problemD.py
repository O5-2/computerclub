from sys import stdin
n, k = [int(i) for i in stdin.readline().split(' ')]
trim = lambda s: s[:-1] if s[-1] == "\n" else s
stages = ''.join(sorted(trim(stdin.readline())))

weight = 0
j = 0
lastStage = "_"
for i in range(0, k):
    while (j < n) and (ord(stages[j]) <= ord(lastStage)+1):
        j += 1
    if j >= n:
        weight = -1
        break
    lastStage = stages[j]
    weight += ord(stages[j])-96

print(weight)
