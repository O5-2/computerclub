from sys import stdin
registered = []
while True:
    reg = stdin.readline()+""
    if reg == "#\n":
        break
    registered.append([int(i) for i in reg.split(' ')[1:]])
registered = sorted(registered)
queries = int(stdin.readline())
q = 0
t = 0
while q != queries:
    t += 1
    for i in registered:
        if t % i[1] == 0:
            print(i[0])
            q += 1
        if q == queries:
            break
