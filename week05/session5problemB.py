from sys import stdin
n = int(stdin.readline())
days = stdin.readline()

more = 0
for i in range(0, n-1):
    if days[i] != days[i+1]:
        if days[i+1] == "F":
            more += 1
        else:
            more -= 1

if (more > 0):
    print("YES")
else:
    print("NO")
