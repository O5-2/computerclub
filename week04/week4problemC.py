from sys import stdin
from math import sqrt

n, k = [int(i) for i in stdin.readline().split(' ')]
solvingTime = 240-k
ans = min(int(sqrt((solvingTime*2)//5)), n)
if (ans*(ans+1)*5)//2 > solvingTime:
    ans -= 1

print(ans)
