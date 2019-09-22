from sys import stdin
n = int(stdin.readline())
A = [int(i) for i in stdin.readline().split(' ')]
B = [int(i) for i in stdin.readline().split(' ')]

ult = 0
pentult = 0
soda = 0
for i in range(0, n):
    soda += A[i]
    ult, pentult = [max(ult, pentult, B[i]), ult+pentult+B[i]-max(ult, pentult, B[i])-min(ult, pentult, B[i])]

if ult+pentult >= soda:
    print("YES")
else:
    print("NO")
