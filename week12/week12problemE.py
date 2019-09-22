from sys import stdin
while True:
    n = int(stdin.readline())
    try:
        nums = sorted([int(i) for i in stdin.readline().split(' ')])
    except ValueError:
        break
#    n = int(stdin.readline())
#    if n == 0:
#        break
    #nums = sorted([int(i) for i in stdin.readline().split(' ')])
    #total = nums[0]
    #cost = 0
    #for i in range(1, len(nums)):
    #    cost += total+nums[i]
    #    total += nums[i]
    #print(cost)
    print(sum([nums[i]*(len(nums)-i) for i in range(0, len(nums))])-nums[0])

# I've made a logical error here. Say that a <= b <= c <= d.
# Adding them in the order ((ab)c)d costs 3a+3b+2c+d.
# But adding them in the order (ab)(cd) costs 2a+2b+2c+d.
# And a+b could be less than *or* greater than d.
