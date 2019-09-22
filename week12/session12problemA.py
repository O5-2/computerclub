from sys import stdin
from collections import defaultdict
trim = lambda s: s[:-1] if (s[-1] == "\n") else s

def sequences(s1, s2):
    d1 = defaultdict(int)
    for i in s1:
        d1[i] += 1
    d2 = defaultdict(int)
    for i in s2:
        d2[i] += 1
    if d1 != d2:
        return False
    if len(s1) == 0:
        return [""]
    if len(s1) == 1:
        return ["i o"]
    ans = []
    cur = ""
    for n in range(0, len(s1)):
        if s1[n] == s2[-1]:
            prefix = sequences(s1[:n], s2[:n])
            insert = sequences(s1[n+1:], s2[n:-1])
            if prefix and insert:
                for x in prefix:
                    for y in insert:
                        cur = ""
                        if x == "":
                            cur += "i "
                        else:
                            cur += x+" i "
                        if y == "":
                            cur += "o"
                        else:
                            cur += y+" o"
                        ans.append(cur)
    return ans

while True:
    s1 = stdin.readline()+""
    if (s1 == "") or (s1 == "\n"):
        break
    s1 = trim(s1)
    s2 = trim(stdin.readline())
    d1 = defaultdict(int)
    for i in s1:
        d1[i] += 1
    d2 = defaultdict(int)
    for i in s2:
        d2[i] += 1
    if d1 != d2:
        print("[\n]")
        continue
    print("[\n"+"\n".join(sorted(sequences(s1, s2)))+"\n]")

# This gets a "Presentation Error" on vjudge, which apparently means I printed something when I wasn't supposed to, but I don't know why.
# I don't have time to fix this or do the other live session 12 problems, because of all my other homework.
