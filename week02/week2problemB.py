from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    S = stdin.readline()[0:]
    if ord(S[-1]) == 10:
        S = S[:-1]
    if ((S[:2]*(len(S)//2) == S) or (S[:2]*(len(S)//2) + S[0] == S)) and (S[0] != S[1]):
        print("YES")
    else:
        print("NO")
