from sys import stdin
n = int(stdin.readline())

num = 0
x = []
for i in range(max(0, n-81), n+1):
    j = i+0
    s = 0
    while j != 0:
         s += j % 10
         j = j // 10
    if i+s == n:
        num += 1
        x.append(i)

print(num)
for i in x:
    print(i)
