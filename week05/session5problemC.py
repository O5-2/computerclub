from sys import stdin
n, k = [int(i) for i in stdin.readline().split(' ')]
boxes = [int(i) for i in stdin.readline().split(' ')]

minRemaining = n
box = 0
for i in range(0, k):
    if ((n % boxes[i]) <= minRemaining):
        minRemaining = n % boxes[i]
        box = i

print(str(box+1) + " " + str(n//boxes[box]))

# So uh... for some bizarre reason, *this* code works,
# but if I initialize box as -1 and set the if condition to ((n % boxes[i]) < minRemaining),
# it doesn't work.
