from sys import stdin
k = [int(i) for i in stdin.readline().split(' ')]

print(256*min(k[0], k[2], k[3]) + 32*min(k[1], k[0]-min(k[0], k[2], k[3])))
