from sys import stdin
n = int(stdin.readline())
h = [int(i) for i in stdin.readline().split(' ')]

minCosts = [0, abs(h[1]-h[0])]
for i in range(2, len(h)):
    minCosts.append(min(abs(h[i]-h[i-2])+minCosts[i-2], abs(h[i]-h[i-1])+minCosts[i-1]))

print(minCosts[-1])
