from sys import stdin
n = int(stdin.readline())

num = 0
for a in range(1, n+1):
    for b in range(a, n+1):
        c = a ^ b
        if ((b <= c) and (c <= n)) and (a+b > c):
                num += 1
           
print(num)
