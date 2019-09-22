from sys import stdin

T = int(stdin.readline())

def gcd(x, y):
     if (x == 0) or (y == 0):
        return x+y
     if x >= y:
        return gcd(y, x % y)
     if y > x:
        return gcd(x, y % x)
     return -1

def lcm(x, y):
     return int(x*y/gcd(x, y))

for i in range(0, T):
    x, y = [int(i) for i in stdin.readline().split(' ')]
    print(str(gcd(x, y)) + ' ' + str(lcm(x, y)))
