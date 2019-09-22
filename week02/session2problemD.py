from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    n = int(stdin.readline())
    A = [int(i) for i in stdin.readline().split(' ')]
    S = sorted(A)
    friends = 0
    for i in S:
        if i > friends:
            break
        friends += 1
    print(friends)
