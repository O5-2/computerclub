from sys import stdin
a = [int(i) for i in stdin.readline().split(' ')]

s = sum(a)
possible = False
for i in range(1, 5):
    for j in range(i+1, 6):
        team = a[0]+a[i]+a[j]
        if team == s-team:
            possible = True

if possible:
    print("YES")
else:
    print("NO")
