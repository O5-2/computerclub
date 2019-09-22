from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    numsLen = int(stdin.readline()) # constant
    nums = [int(i) for i in stdin.readline().split(' ')] # linear
    valids = [i for i in range(numsLen, 0, -1)] # linear
    for i in range(1, numsLen): # quadratic? linear?
        if nums[i] < nums[i-1]:
            for j in range(0, i):
                valids[j] = min(valids[j], i-j)
    print(sum(valids)) # constant

# Is it quadratic time, or linear time?
# Well, it's an improvement, but I think that it's still quadratic.
