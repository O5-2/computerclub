from sys import stdin
n = int(stdin.readline())

winners = []
spectator = 3
possible = True
for i in range(0, n):
    winners.append(int(stdin.readline()))
    if winners[i] == spectator:
        possible = False
        break
    spectator = 6-spectator-winners[i]

if possible:
    print("YES")
else:
    print("NO")
