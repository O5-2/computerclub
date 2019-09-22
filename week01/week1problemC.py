from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    N, K = [int(i) for i in stdin.readline().split(' ')]
    mostCoins = 0
    for i in range(1, K+1):
        mostCoins = max(mostCoins, N % i)
    print(mostCoins)
