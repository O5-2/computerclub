from sys import stdin
n, l, r = [int(i) for i in stdin.readline().split(' ')]
minimum = (n-l+1) + (2*(2**(l-1) - 1))
maximum = (2**r - 1) + (n-r)*(2**(r-1))
print(str(minimum)+' '+str(maximum))
# minimum possible = n-l+1 ones, a [2, 4, 8, ...] of length l-1 
# maximum possible = a [1, 2, 4, 8, ...] of length r, n-r numbers equal to 2^(r-1).
