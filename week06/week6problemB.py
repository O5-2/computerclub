from sys import stdin
n, m = [int(i) for i in stdin.readline().split(' ')]
s = stdin.readline()[:-1]

trim = lambda s: s[:-1] if (s[-1] == "\n") else s

for i in range(0, m):
    data = trim(stdin.readline().split(' '))
    l = int(data[0])
    r = int(data[1])
    c1 = data[2]
    c2 = trim(data[3])
    for i in range(l-1, r):
        if s[i] == c1:
            s = s[:i]+c2+s[i+1:]

print(s)
