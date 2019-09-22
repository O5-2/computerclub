from sys import stdin
letters = stdin.readline()+""

Qs = 0
for i in letters:
    if i == "Q":
        Qs += 1

totalQAQ = 0
curQs = 0
for i in letters:
    if i == "Q":
        curQs += 1
    elif i == "A":
        totalQAQ += curQs*(Qs-curQs)

print(totalQAQ)
