from sys import stdin

T = int(stdin.readline())
testcases = []
# testcases will be a list. Each element of testcases will be a list, with first element int (K) and second element a list of ints (A).

for i in range(0, T):
    N, K = [int(x) for x in stdin.readline().split(' ')]
    A = [int(x) for x in stdin.readline().split(' ')]
    valid = False
    for i in range(0, len(A)):
        if (K - A[i]) in A:
            if (K - A[i]) == A[i]:
                copies = 0
                for j in A:
                    if j == A[i]:
                        copies += 1
                if copies > 1:
                    valid = True
            else:
                valid = True
    if valid:
        print("Yes")
    else:
        print("No")
