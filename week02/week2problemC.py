from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    a, b = [int(i) for i in stdin.readline().split(' ')]
    num = []
    while (a != 0) or (b != 0):
        num.append(((a % 10)+(b % 10)) % 10)
        a = a // 10
        b = b // 10
    num = [num[i]*(10**i) for i in range(0, len(num))]
    print(sum(num))
