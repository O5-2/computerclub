from sys import stdin
a, b = [int(i) for i in stdin.readline().split(' ')]

ans = 0
if b < a+5:
    ans = 1
    for i in range(a+1, b+1):
        ans = (ans*(i % 10)) % 10
print(ans)
