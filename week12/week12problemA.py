import sys
from collections import defaultdict
cycles = defaultdict(int)
for line in sys.stdin:
    try:
        i, j = [int(x) for x in line.split(' ')]
    except ValueError:
        break
    n, m = sorted([i, j])
    for k in range(n, m+1):
        if k not in cycles:
            length = 1
            num = k
            while num != 1:
                if num % 2 == 0:
                    num /= 2
                else:
                    num = (3*num)+1
                length += 1
            cycles[k] = length
    print(str(i)+" "+str(j)+" "+str(max([cycles[x] for x in range(n, m+1)])))

# I think I've made a logical error, or failed to account for an edge case, or something, because it gives me a Wrong Answer.
