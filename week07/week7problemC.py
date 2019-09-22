from sys import stdin
n = int(stdin.readline())

if (n % 2 == 0):
    print(int(2**(n/2)))
else:
    print(0)
