from sys import stdin
from math import ceil
n, a, b = [int(i) for i in stdin.readline().split(' ')]
colors = [int(i) for i in stdin.readline().split(' ')]

price = 0
for i in range(0, ceil(n/2)):
    if set([colors[i], colors[-(i+1)]]) == set([0, 2]):
        price += a
    elif set([colors[i], colors[-(i+1)]]) == set([1, 2]):
        price += b
    elif set([colors[i], colors[-(i+1)]]) == set([2]):
        price += (2-(i == ceil(n/2)-1 and n % 2 == 1))*min(a, b)
    elif set([colors[i], colors[-(i+1)]]) == set([0, 1]):
        price = -1
        break

print(price)
