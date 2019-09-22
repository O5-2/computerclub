from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    A = int(stdin.readline())
    profit = A-1
    day = 1
    maxValue = 0
    maxDay = 0
    while profit >= 0:
        profit = profit + A - 2**day
        day += 1
        if profit > maxValue:
            maxValue = profit
            maxDay = day
    day -= 1
    print(str(day) + ' ' + str(maxDay))
