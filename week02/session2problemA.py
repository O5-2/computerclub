from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    n, q = [int(i) for i in stdin.readline().split(' ')]
    D = [int(i) for i in stdin.readline().split(' ')]
    queries = [int(i) for i in stdin.readline().split(' ')]
    answers = ""
    prod = 1
    for i in range(0, n):
        prod *= D[i]
    for i in range(0, q):
        answers += (str(queries[i] // prod) + ' ')
    answers = answers[:-1]
    print(answers)
