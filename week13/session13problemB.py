from sys import stdin
n, k = [int(i) for i in stdin.readline().split(' ')]
h = [int(i) for i in stdin.readline().split(' ')]

minCosts = [0, abs(h[1]-h[0])]
for i in range(2, len(h)):
    minCosts.append(min([abs(h[i]-h[i-j])+minCosts[i-j] for j in range(1, min(i, k)+1)]))

print(minCosts[-1])
