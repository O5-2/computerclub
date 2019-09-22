from sys import stdin
n = int(stdin.readline())
moves = stdin.readline()

wallDistance = 0
side = 0
coins = 0
for i in range(0, n):
    if moves[i] == "U":
        wallDistance += 1
    else:
        wallDistance -= 1
    if wallDistance > 0:
        if side == 2:
            coins += 1
        side = 1
    elif wallDistance < 0:
        if side == 1:
            coins += 1
        side = 2

print(coins)
