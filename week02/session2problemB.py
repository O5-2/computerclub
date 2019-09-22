from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    n = int(stdin.readline())
    A = [int(i) for i in stdin.readline().split(' ')]
    S = set(A)
    b = True
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if not (A[i]*A[j] in S):
                b = False
    if b:
        print("yes")
    else:
        print("no")


# Currently quadratic time. Not sure how to make it faster, really.
